import argparse

def parse_args():
   '''
   Parses the node2vec arguments.
   '''
   parser = argparse.ArgumentParser(description="Run node2vec.")

   # ===================== I/O ===================== #
   parser.add_argument('--input', type=str, default='../graph/karate.edgelist',
                       help='Input graph path')
   parser.add_argument('--labels', type=str, default='../graph/karate.labels',
                       help='Label per node of graph')
   parser.add_argument('--output_dir_name', type=str, default=None,
                       help='Name of output directory')
   parser.add_argument('--loc_results_dir', type=str, default="../results",
                       help='Location of results')
   parser.add_argument('--output', type=str, default=None,
                       help='User-specified output location')
   # =============================================== #
   
   # ========= Skip-gram training settings ========= #
   parser.add_argument('--seed', default=42, type=int,
                       help='Random seed')
   parser.add_argument('--epochs', default=1, type=int,
                       help='Number of epochs in SGD')
   parser.add_argument('--workers', type=int, default=8,
                       help='Number of parallel workers. Default is 8.')
   # =============================================== #

   # ===== (Bayesian) Optimization parameters  ===== #
   parser.add_argument('--train_set', default=0.8, type=float,
                       help='Portion of dataset used for optimization')
   parser.add_argument('--bayesian_opt', action='store_true',
                       help='Enable bayesian optimization')
   parser.add_argument('--iter_bayesian', default=50, type=int,
                       help='Number of iterations for bayesian optimization')
   parser.add_argument('--scoring', default="f1_macro", type=str,
                       help='How to evaluate each iteration of bayesian opt')
   parser.add_argument('--cross_validation', default=10, type=int,
                       help='Size of cross validation')
   parser.add_argument('--replications', default=5, type=int,
                       help='Number of replications to evaluate hyperparameter config')
   # =============================================== #

   # ==== Original Hyperparameter configuration ==== #
   parser.add_argument('--d', type=int, default=128,
                       help='Number of dimensions. Default is 128.')
   parser.add_argument('--l', type=int, default=100,
                       help='Length of walk per source. Default is 100.')
   parser.add_argument('--r', type=int, default=16,
                       help='Number of walks per source. Default is 18.')
   parser.add_argument('--k', type=int, default=14,
                       help='Context size for optimization. Default is 16.')
   
   # ==== Parameters Added/Modified for partitions
   parser.add_argument('--p', nargs='+', default=[1.],
                      help='Return hyperparameter. Default is 1.')
   parser.add_argument('--q', nargs='+', default=[1.],
                      help='Return hyperparameter. Default is 1.')
   parser.add_argument('--partitions', type=int, default=1,
                      help='Amout of partitions of dimensionality')
   # =============================================== #

   # ==== Restart probability related arguments ==== #
   parser.add_argument('--restarts', action="store_true",
                     help='Enable restart probability')
   parser.add_argument('--tau', type=float, default=0.001,
                     help='Min. restart probability, irrespective of degree')
   parser.add_argument('--omega', type=float, default=2.0,
                     help='Scalar for r (i.e., no. random walks per node)')
   parser.add_argument('--epsilon', type=float, default=0.0001,
                     help='Max. restart probability for nodes with high degrees')
   parser.add_argument('--s', type=int, default=10,
                     help='Min. length of all biased random walks')
   # =============================================== #

   # ================= Graph type self.model = Word2Vec( ================= #
   parser.add_argument('--weighted', dest='weighted', action='store_true',
                     help='Boolean specifying (un)weighted. Default is unweighted.')
   parser.add_argument('--unweighted', dest='unweighted', action='store_false')
   parser.set_defaults(weighted=False)

   parser.add_argument('--directed', dest='directed', action='store_true',
                     help='Graph is (un)directed. Default is undirected.')
   parser.add_argument('--undirected', dest='undirected', action='store_false')
   parser.set_defaults(directed=False)
   # =============================================== #

   return parser.parse_args()
