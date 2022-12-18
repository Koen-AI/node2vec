#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.edgelist --labels /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.labels  --output /data/s1674307/snacs/Results/email-Eu-core/results_partitions_4_email_log_sigma --train_set 0.8 --directed --seed 24034 --partitions 4 --p 0.20055087005505193 0.20020465693121992 4.0 4.0 --q 3.9964945282600097 0.20324601704201256 2.045629250781856 1.8984324672375856


#std:
#lambda =  0.01228759817
#p-list =  [0.20055087005505193, 0.20020465693121992, 4.0, 4.0]
#q-list =  [3.9964945282600097, 0.20324601704201256, 2.045629250781856, 1.8984324672375856]
