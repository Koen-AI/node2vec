#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/facebook/facebook.edgelist --labels /data/s1674307/snacs/Datasets/facebook/facebook.labels  --output /data/s1674307/snacs/Results/facebook/results_partitions_2_facebook_log_sigma --train_set 0.8 --directed --seed 22038 --partitions 2 --p 3.952918871253783 0.2582509494247336 --q 3.882408596560285 0.20001483371562215

#std:
#lambda =  0.0096750859
#p-list =  [3.952918871253783, 0.2582509494247336] 
#q-list =  [3.882408596560285, 0.20001483371562215]
