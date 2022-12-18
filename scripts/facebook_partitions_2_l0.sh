#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/facebook/facebook.edgelist --labels /data/s1674307/snacs/Datasets/facebook/facebook.labels  --output /data/s1674307/snacs/Results/facebook/results_partitions_2_facebook_l0 --train_set 0.8 --directed --seed 22138 --partitions 2 --p 0.7572958018829294 3.952918871253783 --q 1.473612599456155 3.882408596560285

#2:
#lambda =  0.0
#p-list =  [0.7572958018829294, 3.952918871253783]
#q-list =  [1.473612599456155, 3.882408596560285]
