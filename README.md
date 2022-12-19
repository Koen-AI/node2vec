# node2vec

This repository provides a reference implementation of *node2vec* as described in the paper:<br>
> node2vec: Scalable Feature Learning for Networks.<br>
> Aditya Grover and Jure Leskovec.<br>
> Knowledge Discovery and Data Mining, 2016.<br>
> <Insert paper link>

The *node2vec* algorithm learns continuous representations for nodes in any (un)directed, (un)weighted graph. Please check the [project page](https://snap.stanford.edu/node2vec/) for more details. 

### Basic Usage

#### Example
To run *node2vec* on the email-Eu-core dataset, execute the following command from the project home directory:<br/>
	``python src/main.py --input email-Eu-core.edgelist --labels email-Eu-core.labels --output results-email-Eu-core``

#### Options
You can check out the other options available to use with *node2vec* using:<br/>
	``python src/main.py --help``

#### Options added with the added functionality 
We have added the following parameters to configure the added functionality:
  - To configure the bayesian optimisation:
    * ``--train_set`` to specify the proportion of dataset used for optimisation
    * ``--bayesian_opt`` to toggle Enable bayesian optimisation
    * ``--iter_bayesian`` to specify the number of iterations for bayesian optimisation
    * ``--scoring`` to specify how to evaluate each iteration of bayesian optimisation
    * ``--cross_validation`` to specify the size of cross validation 
    * ``--replications`` to specify the number of replications to evaluate hyperparameter configuration
  - To configure the restart method:
    * ``--restarts`` to toggle the restart functionality
    * ``--tau`` to set the $tau$ parameter
    * ``--omega`` to set the $\omega$ parameter
    * ``--epsilon`` to set the $\varepsilon$ parameter
    * ``--s`` to set the $s$ parameter
  - To configure the ensemble method:
    * ``--partitions`` to define how many ensembles you want
    * ``--p`` now also supports a sequence of floats
    * ``--q`` now also supports a sequence of floats

#### post processing
To find the $\lambda$ and/or $p,q$-lists to use for partitions you can use ``post_processing.py`` 

#### Example post processing
To run *post_process* on the email-Eu-core dataset, execute the following command from the project home directory:<br/>
  ``python src/post_process.py --dir results-email-Eu-core --partitions 4 --read --write``
To run learn about the options for *post_process* execute the following command from the project home directory:<br/>
  ``python src/post_process.py --help``

#### Input
The supported input format is an edgelist:

	node1_id_int node2_id_int <weight_float, optional>
		
The graph is assumed to be undirected and unweighted by default. These options can be changed by setting the appropriate flags.

#### Output
The output file directory contains the following
 - ``cl_args.json``: a file with the settings of all the calleble arguments
 - The ``eval`` directory, which contains the following:
   * directories for each replication with an embeddings.pkl file containing the vector embedding of the input graph for that replication
   * ``results.csv``: a file with the results of the classifier over all replications
   * ``best_settings.json``: a file that contains the best settings for each calleble argument
 - If the program was called with the ``--bayesian_opt`` flag the following will also be in the output directory:
   * ``BO_opt*.pdf``: a plot of the bayesian optimisation
   * ``opt_results.pkl``: the scores of each configuration of the bayesian optimisation run
### Citing
If you find *node2vec* useful for your research, please consider citing the following paper:

	@inproceedings{node2vec-kdd2016,
	author = {Grover, Aditya and Leskovec, Jure},
	 title = {node2vec: Scalable Feature Learning for Networks},
	 booktitle = {Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
	 year = {2016}
	}


### Miscellaneous

Please send any questions you might have about the code and/or the algorithm to <adityag@cs.stanford.edu>.

*Note:* This is only a reference implementation of the *node2vec* algorithm and could benefit from several performance enhancement schemes, some of which are discussed in the paper.
