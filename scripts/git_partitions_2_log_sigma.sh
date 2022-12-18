#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/git/git.edgelist --labels /data/s1674307/snacs/Datasets/git/git.labels  --output /data/s1674307/snacs/Results/git/results_partitions_2_git_log_sigma --train_set 0.8 --directed --seed 22091 --partitions 2 --p 3.9045821112145163 0.20044094569330795 --q 3.9816568985190535 0.9203925397880377

#std:
#lambda =  0.00781529216
#p-list =  [3.9045821112145163, 0.20044094569330795]
#q-list =  [3.9816568985190535, 0.9203925397880377]
