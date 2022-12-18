#!/bin/bash

# Bayesian Opt
python3 -W ignore ../src/main.py --bayesian_opt --iter_bayesian 3 --loc_results_dir ../../res

# Restarts + Bayesian Opt
python3 -W ignore ../src/main.py --bayesian_opt --iter_bayesian 3 --restarts

# Partitions + Bayesian Opt
python3 -W ignore ../src/main.py --bayesian_opt --iter_bayesian 3 --partitions 2 --q 0.1 0.2 --p 0.1 0.2

# Partitions + Restarts + Bayesian Opt
python3 -W ignore ../src/main.py --bayesian_opt --iter_bayesian 3 --partitions 2 --restarts --q 0.1 0.2 --p 0.1 0.2