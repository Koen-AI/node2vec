#!/bin/bash

# Bayesian Opt
python ../src/main.py --input /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.edgelist --labels /data/s1674307/snacs/Datasets/email-Eu-core/email-Eu-core.labels  --output /data/s1674307/snacs/Results/email-Eu-core/results_baseline_email --train_set 0.8 --directed --seed 20234 --p 4.0 --q 1.8984324672375856
