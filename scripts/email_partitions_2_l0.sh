#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.edgelist --labels /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.labels  --output /data/s1674307/snacs/Results/email-Eu-core/results_partitions_2_email_l0 --train_set 0.8 --directed --seed 22134 --partitions 2 --p 4.0 4.0 --q 2.045629250781856 1.8984324672375856


#2:
#lambda =  0.0
#p-list =  [4.0, 4.0]
#q-list =  [2.045629250781856, 1.8984324672375856]

