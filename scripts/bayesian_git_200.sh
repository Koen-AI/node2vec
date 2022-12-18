#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/git/git.edgelist --labels /data/s1674307/snacs/Datasets/git/git.labels  --output /data/s1674307/snacs/Results/git/results_bayesian_git --bayesian_opt --iter_bayesian 200 --train_set 0.1 --directed --seed 20091
