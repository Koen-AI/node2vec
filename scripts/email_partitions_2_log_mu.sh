#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.edgelist --labels /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.labels  --output /data/s1674307/snacs/Results/email-Eu-core/results_partitions_2_email_log_mu --train_set 0.8 --directed --seed 22334 --partitions 2 --p 0.20020465693121992 3.9485236573580504 --q 0.20324601704201256 3.9989870044384537


#mean:
#lambda =  0.35799953691
#p-list =  [0.20020465693121992, 3.9485236573580504]
#q-list =  [0.20324601704201256, 3.9989870044384537]
