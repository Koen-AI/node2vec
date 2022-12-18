#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.edgelist --labels /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.labels  --output /data/s1674307/snacs/Results/email-Eu-core/results_restarts_email --bayesian_opt --iter_bayesian 200 --train_set 0.1 --directed --seed 20234 --restarts --p 4.0 --q 1.8984324672375856
