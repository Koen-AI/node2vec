#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/facebook/facebook.edgelist --labels /data/s1674307/snacs/Datasets/facebook/facebook.labels  --output /data/s1674307/snacs/Results/facebook/results_restart_facebook --bayesian_opt --iter_bayesian 200 --train_set 0.1 --directed --seed 20238 --restarts --p 0.7572958018829294 --q 1.473612599456155
