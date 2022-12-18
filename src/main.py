import os
import datetime
import json
import pickle
from command_line import parse_args
from model import Model
from plot_bayes_opt import plot_heatmap
from sklearn.utils.estimator_checks import check_estimator
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, recall_score, precision_score, accuracy_score
from skopt import BayesSearchCV
from skopt.space import Real, Integer

def bayes_opt_pq(args, X_train, y_train, DIR):
   opt = BayesSearchCV(
      Model(r=args.r, d=args.d, l=args.l, k=args.k, restarts=args.restarts, \
            tau=args.tau, omega=args.omega, epsilon=args.epsilon, s=args.s, \
            weighted=args.weighted, directed=args.directed, epochs=args.epochs, \
            nodes=args.input, dir_base=None),
      {
         'p': Real(0.2, 4, prior='log-uniform'),
         'q': Real(0.2, 4, prior='log-uniform')
      },
      n_iter=args.iter_bayesian,
      cv=args.cross_validation,
      scoring=args.scoring,
      verbose=1,
      random_state=args.seed,
      n_jobs=args.workers,
      optimizer_kwargs={'n_initial_points': 64, 'initial_point_generator': "grid"}
   )
   opt.fit(X_train, y_train)
   with open(f"{DIR}/opt_results.pkl", 'wb') as f:
      pickle.dump(opt.cv_results_, f)
   plot_heatmap(DIR, args.restarts)

   p = opt.best_params_['p']
   q = opt.best_params_['q']
   return p, q

def bayes_opt_restarts(args, X_train, y_train, DIR):
   opt = BayesSearchCV(
      Model(p=args.p, q=args.q, r=args.r, d=args.d, l=args.l, \
            k=args.k, restarts=args.restarts, epsilon=args.epsilon, s=args.s, \
            weighted=args.weighted, directed=args.directed, epochs=args.epochs, \
            nodes=args.input, dir_base=None),
      {
         'omega':     Real(0.1, 4.0, prior='log-uniform'),
         'epsilon':   Real(0.001, 0.15, prior='log-uniform')
      },
      n_iter=args.iter_bayesian,
      cv=args.cross_validation,
      scoring=args.scoring,
      verbose=1,
      random_state=args.seed,
      n_jobs=args.workers,
      optimizer_kwargs={'n_initial_points': 64, 'initial_point_generator': "grid"}
   )
   opt.fit(X_train, y_train)
   with open(f"{DIR}/opt_results.pkl", 'wb') as f:
      pickle.dump(opt.cv_results_, f)
   plot_heatmap(DIR, args.restarts)

   omega = opt.best_params_['omega']
   tau = opt.best_params_['tau']
   return omega, tau

def evaluate(args, train_X, train_y, test_X, test_y, DIR):
   dir_out = f"{DIR}/eval"
   os.mkdir(dir_out)

   with open(f"{dir_out}/best_settings.json", 'w') as f:
      json.dump(args.__dict__, f, indent=3)

   with open(f"{dir_out}/results.csv", 'w') as f_out:
      f_out.write("F1_macro,F1_micro,accuracy\n")
      for i in range(args.replications):
         # Create model
         m = Model(p=args.p, q=args.q, r=args.r, d=args.d, \
                   l=args.l, k=args.k, restarts=args.restarts, \
                   tau=args.tau, omega=args.omega, epsilon=args.epsilon, \
                   s=args.s, weighted=args.weighted, directed=args.directed, \
                   epochs=args.epochs, nodes=args.input, dir_base=dir_out, \
                   partitions=args.partitions)
         m.fit(train_X, train_y)

         pred_y = m.predict(test_X)

         f1_macro = f1_score(test_y, pred_y, average="macro")
         f1_micro = f1_score(test_y, pred_y, average="micro")
         accuracy = accuracy_score(test_y, pred_y)

         f_out.write(f"{f1_macro},{f1_micro},{accuracy}\n")

if __name__ == "__main__":
   args = parse_args()
   
   arg_len = args.partitions
   q_len = len(args.q)
   p_len = len(args.p)
  
   q_error = "Error: expected q-list to have: " + str(arg_len) + " parameters but got: " + str(q_len) + " parameters!"
   p_error = "Error: expected p-list to have: " + str(arg_len) + " parameters but got: " + str(p_len) + " parameters!"
  
   assert q_len == arg_len, q_error
   assert p_len == arg_len, p_error
   assert args.d % arg_len == 0, "Error: dimensions must be divisible by partitions"

   if not os.path.isdir(args.loc_results_dir):
      os.mkdir(args.loc_results_dir)
   
   if args.output is not None:
      DIR = f"{args.output}"
   elif args.output_dir_name is not None:
      DIR = f"{args.loc_results_dir}/{args.output_dir_name}"
   else:
      t = datetime.datetime.now()
      DIR = f"{args.loc_results_dir}/results_{t.day}-{t.month}-{t.year}_{t.hour}-{t.minute}-{t.second}"
   os.mkdir(DIR)
   with open(f"{DIR}/cl_args.json", 'w') as f:
      json.dump(args.__dict__, f, indent=3)

   # Obtain nodes and corresponding labels from dataset
   X, y = [], []
   with open(args.labels, 'r') as f_labels:
      data = f_labels.read()
      lines = data.split('\n')
      lines = lines[:-1]
      for line in lines:
         xy = line.split('\t')
         X.append(xy[0])
         y.append(xy[1])
   
   X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=args.train_set)

   if args.bayesian_opt:
      if args.restarts:  # Optimize omega, epsilon
         args.omega, args.tau = bayes_opt_restarts(args, X_train, y_train, DIR)
      else:  # Optimize p and q
         p, q = bayes_opt_pq(args, X_train, y_train, DIR)
         args.p[0] = p
         args.q[0] = q
         
   #TODO else:
   evaluate(args, X_train, y_train, X_test, y_test, DIR)
