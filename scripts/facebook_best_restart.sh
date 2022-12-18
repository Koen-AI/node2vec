#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/facebook/facebook.edgelist --labels /data/s1674307/snacs/Datasets/facebook/facebook.labels --output /data/s1674307/snacs/Results/facebook/results_best_restart_facebook --train_set 0.8 --directed --seed 20438 --restarts --p 0.7572958018829294 --q 1.473612599456155 --omega 0.14421504937982915 --epsilon 0.028564075866728048
