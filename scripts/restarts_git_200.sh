#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/git/git.edgelist --labels /data/s1674307/snacs/Datasets/git/git.labels  --output /data/s1674307/snacs/Results/git/results_restart_git --bayesian_opt --iter_bayesian 200 --train_set 0.1 --directed --seed 20291 --restarts --p 0.20044094569330795 --q 0.9203925397880377
