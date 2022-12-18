#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/facebook/facebook.edgelist --labels /data/s1674307/snacs/Datasets/facebook/facebook.labels  --output /data/s1674307/snacs/Results/facebook/results_partitions_4_facebook_log_sigma --train_set 0.8 --directed --seed 24038 --partitions 4 --p 0.2789901587924842 3.952918871253783 0.2582509494247336 3.932640274977744 --q 2.8674846577475455 3.882408596560285 0.20001483371562215 0.20123973200915848

#std:
#lambda =  0.00432788555
#p-list =  [0.2789901587924842, 3.952918871253783, 0.2582509494247336, 3.932640274977744]
#q-list =  [2.8674846577475455, 3.882408596560285, 0.20001483371562215, 0.20123973200915848]
