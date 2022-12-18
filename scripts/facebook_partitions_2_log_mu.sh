#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/facebook/facebook.edgelist --labels /data/s1674307/snacs/Datasets/facebook/facebook.labels  --output /data/s1674307/snacs/Results/facebook/results_partitions_2_facebook_log_mu --train_set 0.8 --directed --seed 22338 --partitions 2 --p 0.20035678700497078 3.9624962332158433 --q 3.9346541105982795 0.20002695371111892

#mean:
#lambda =  0.35799953691
#p-list =  [0.20035678700497078, 3.9624962332158433]
#q-list =  [3.9346541105982795, 0.20002695371111892]
