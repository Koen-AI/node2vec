#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/git/git.edgelist --labels /data/s1674307/snacs/Datasets/git/git.labels  --output /data/s1674307/snacs/Results/git/results_partitions_2_git_log_mu --train_set 0.8 --directed --seed 22391 --partitions 2 --p 3.9918006380440088 0.2006002451797317 --q 0.21978237126151454 3.983347440320607

#mean:
#lambda =  0.76243839424
#p-list =  [3.9918006380440088, 0.2006002451797317]
#q-list =  [0.21978237126151454, 3.983347440320607]
