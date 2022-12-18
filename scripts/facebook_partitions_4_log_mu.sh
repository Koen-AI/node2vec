#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/facebook/facebook.edgelist --labels /data/s1674307/snacs/Datasets/facebook/facebook.labels  --output /data/s1674307/snacs/Results/facebook/results_partitions_4_facebook_log_mu --train_set 0.8 --directed --seed 24338 --partitions 4 --p 4.0 0.20035678700497078 3.9624962332158433 0.20343128081760056 --q 4.0 3.9346541105982795 0.20002695371111892 0.20319502640848378

#p-list =  [4.0, 0.20035678700497078, 3.9624962332158433, 0.20343128081760056]
#q-list =  [4.0, 3.9346541105982795, 0.20002695371111892, 0.20319502640848378]
