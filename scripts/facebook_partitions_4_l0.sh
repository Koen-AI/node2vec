#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/facebook/facebook.edgelist --labels /data/s1674307/snacs/Datasets/facebook/facebook.labels  --output /data/s1674307/snacs/Results/facebook/results_partitions_4_facebook_l0 --train_set 0.8 --directed --seed 24138 --partitions 4 --p 0.7572958018829294 0.43847646369464355 0.5441322973617186 3.952918871253783 --q 1.473612599456155 1.356481752864832 1.4738792294786813 3.882408596560285

#4:
#lambda =  0.0
#p-list =  [0.7572958018829294, 0.43847646369464355, 0.5441322973617186, 3.952918871253783]
#q-list =  [1.473612599456155, 1.356481752864832, 1.4738792294786813, 3.882408596560285]
