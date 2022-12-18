#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.edgelist --labels /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.labels  --output /data/s1674307/snacs/Results/email-Eu-core/results_partitions_2_email_log_sigma --train_set 0.8 --directed --seed 22034 --partitions 2 --p 0.20020465693121992 4.0 --q 0.20324601704201256 1.8984324672375856


#std:
#lambda =  0.02614553577
#p-list =  [0.20020465693121992, 4.0]
#q-list =  [0.20324601704201256, 1.8984324672375856]
