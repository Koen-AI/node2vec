import numpy as np
import itertools
import argparse

from math import comb
import csv


def parse_args():
   '''
   Parses the node2vec arguments.
   '''
   parser = argparse.ArgumentParser(description="Run post-processing.")

   # ===================== I/O ===================== #
   parser.add_argument('--pkl', type=str, default="opt_results.pkl",
                       help='Input pkl path')
   parser.add_argument('--scores', type=str, default='scores.csv',
                       help='where to put the table')
   parser.add_argument('--dataset', type=str, default=None,
                       help='Name of dataset; mutually exclusive with the ')
   parser.add_argument('--dir', type=str, default=None,
                       help='Path to fil locations')
   # =============================================== #
   
   # =============== Hyperparameters =============== #
   parser.add_argument('--partitions', default=1, type=int,
                       help='Amount of ensembles/partitions used')
   parser.add_argument('--bayesopts', default=200, type=int,
                       help='Amount of bayesian optimisations run')
   parser.add_argument('--lamb', default=-1.0, type=float,
                       help='weight of the distance distribution')
   parser.add_argument('--logspace', dest='logspace', action='store_true',
                     help='should p-q distances be logarithmic or not?')
   parser.set_defaults(weighted=False)
   # =============================================== #

   # ================ read or write ================ #
   parser.add_argument('--read', dest='read', action='store_true',
                     help='process scores from .csv')
   parser.set_defaults(weighted=False)

   parser.add_argument('--write', dest='write', action='store_true',
                     help='write scores to .csv')
   parser.set_defaults(directed=False)
   # =============================================== #

   return parser.parse_args()


def find_best(A, bayesopts):
    highscore = -1
    omega = -1
    epsilon = -1
    for i in range(bayesopts):
        if A["mean_test_score"][i] > highscore:
            highscore = A["mean_test_score"][i]
            omega = A["param_omega"][i]
            epsilon = A["param_epsilon"][i]

    print("--omega", omega, "--epsilon", epsilon)

def read_scores(A, scores_file, lamb):
    highscore = -1.0
    best_params = "(0, 1, 2, 3)"
    
    with open (scores_file, 'r') as f:
        for line in f.readlines():
            split_line = line.split(";")
            
            f1_score = float(split_line[1])
            dist_score = float(split_line[2])
            score = f1_score + (lamb*dist_score)
            
            if (score > highscore):
                highscore = score
                best_params = split_line[0]
            #if best
        #for line
        final_params = best_params[1:-1].split(',')
        
        p_list = []
        q_list = []
        for param in final_params:
            p_list.append(A["param_p"][int(param)])
            q_list.append(A["param_q"][int(param)])
        
        print("\nlambda = ", lamb)
        print("p-list = ", p_list)
        print("q-list = ", q_list)
        

def write_scores(A, scores_file, partitions, bayesopts, log_space=True):
    f1_score_list = []
    dist_score_list = []
    
    pqs = itertools.combinations(range(bayesopts), partitions)

    with open (scores_file, 'w') as f:
        writer = csv.writer(f, delimiter=';')
        
        for pq in pqs:
            f1_score = 0
            dist_score = 0
            
            for i in range(partitions):  # partitions = len(pq) #by definition
                f1_score += A["mean_test_score"][pq[i]]
                for j in range(i+1, partitions):
                    if log_space:
                        print("log")
                        dist_score += np.sqrt((np.log(A["param_p"][pq[i]]) - np.log(A["param_p"][pq[j]]))**2 + (np.log(A["param_q"][pq[i]]) - np.log(A["param_q"][pq[j]]))**2)
                    else:
                        dist_score += np.sqrt((A["param_p"][pq[i]] - A["param_p"][pq[j]])**2 + (A["param_q"][pq[i]] - A["param_q"][pq[j]])**2)
                        print("else")
                    #if/else
                #for j
            #for i
                
            f1_score_list.append(f1_score)
            dist_score_list.append(dist_score)
            
            row = [pq, f1_score, dist_score]
            
            writer.writerow(row)
        #for pq
    #with open
    
    dist_mean = np.mean(dist_score_list)
    dist_std = np.std(dist_score_list)
    
    f1_mean = np.mean(f1_score_list)
    f1_std = np.std(f1_score_list)
    
    lamb_mean = f1_mean / dist_mean
    lamb_std = f1_std / dist_std
    
    print("\n\ndist-scores:")
    print("The mean score is ", dist_mean)
    print("The standard deviation is ", dist_std)

    print("\n\nF1-scores:")
    print("The mean score is ", np.mean(f1_mean))
    print("The standard deviation is ", np.std(f1_std))
    
    print("lambda_mean = ", lamb_mean)
    print("lambda_std = ", lamb_std)
    
    return lamb_mean, lamb_std


if __name__ == "__main__":
    args = parse_args()

    assert (args.read or args.write or args.partitions == 1), "You must specify to read or write"
    
    data_set = args.dataset

    pkl_file = args.pkl
    scores_file = args.scores
    
    if data_set != None:
        scores_file = scores_file [:-4]  # -= ".csv"
        scores_file += "_" + str(args.partitions) + "_" + data_set + ".csv"
        pkl_file = data_set + "_" + args.pkl
    
    if args.dir != None:
        if args.dir[-1] == '/':
            scores_file = args.dir + scores_file
            pkl_file = args.dir + pkl_file
        else:
            scores_file = args.dir + "/" + scores_file
            pkl_file = args.dir + "/" + pkl_file

    A = np.load(pkl_file, allow_pickle=True)

    
    if args.partitions == 1:
        find_best(A, args.bayesopts)
    
    else:
        if args.write:
            lamb_mean, lamb_std = write_scores(A, scores_file, args.partitions, args.bayesopts, log_space=args.logspace)
            read_scores(A, scores_file, lamb_mean)
            read_scores(A, scores_file, lamb_std)
            
        elif args.read:
            assert (args.lamb > -0.001), "Please specify a valid lamb!"
            read_scores(A, scores_file, args.lamb)








