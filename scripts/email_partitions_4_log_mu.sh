#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.edgelist --labels /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.labels  --output /data/s1674307/snacs/Results/email-Eu-core/results_partitions_4_email_log_mu --train_set 0.8 --directed --seed 24334 --partitions 4 --p 0.20055087005505193 3.86869464452510942 0.20020465693121992 3.9485236573580504 --q 3.9964945282600097 0.20473325176637816 0.20324601704201256 3.9989870044384537


#mean:
#lambda =  0.11933317897
#p-list =  [0.20055087005505193, 3.8686946445251094, 0.20020465693121992, 3.9485236573580504]
#q-list =  [3.9964945282600097, 0.20473325176637816, 0.20324601704201256, 3.9989870044384537]
