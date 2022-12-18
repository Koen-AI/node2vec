import networkx as nx
import datetime
import os
import numpy as np
import pickle
from node2vec import Node2Vec
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_X_y
from gensim.models import Word2Vec
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score, accuracy_score

EMBEDDING_F_OUT = "embeddings.emb"
EMBEDDING_F_OUT_PKL = "embeddings.pkl"

class Model(BaseEstimator):

   def __init__(self, p=[1.0], q=[1.0], r=10, d=128, l=80, k=10, \
                restarts=False, tau=0., omega=2, epsilon=0.01, s=10, \
                epochs=1, weighted=False, directed=False, nodes=None, \
                dir_base=None, partitions=1):
      '''
      Hyperparameter configuration
      '''
      # Hyperparameters for node2vec     
      self.p = p   # Return hyperparameter
      self.q = q   # In-out hyperparameter
      self.r = r   # No. random walks per node
      self.d = d   # Dimensionality of vector embedding
      self.l = l   # Length of one random walk
      self.k = k   # Sliding-window size
      
      #hyperparams for partitions
      self.partitions = partitions  # How many different models to concatinate

      # Hyperparameters for restarts
      self.restarts = restarts   # Enable restarts
      self.tau = tau             # Min. restart probability
      self.omega = omega         # Scalar for r
      self.epsilon = epsilon     # Max. restart prob for nodes with high degree
      self.s = s                 # Min. length of all biased random walks

      self.weighted = weighted
      self.directed = directed
      self.epochs = epochs

      self.nodes = nodes  # File to import the graph into networkx

      self.dir_out = dir_base
      if dir_base is not None:
         t = datetime.datetime.now()
         self.dir_out = f"{dir_base}/run_{t.day}-{t.month}-{t.year}_{t.hour}-{t.minute}-{t.second}-{t.microsecond}"
         os.mkdir(self.dir_out) 

   def _read_graph(self):
      '''
      Reads the input network in networkx.
      '''
      if self.weighted:
         G = nx.read_edgelist(self.nodes, delimiter='\t', nodetype=int, data=(('weight',float),), create_using=nx.DiGraph())
      else:
         G = nx.read_edgelist(self.nodes, delimiter='\t', nodetype=int, create_using=nx.DiGraph())
         for edge in G.edges():
            G[edge[0]][edge[1]]['weight'] = 1

      if not self.directed:
         G = G.to_undirected()

      return G

   def _learn_embeddings(self, walks, part_d):
      # Convert each vertex ID to a string
      walks = [list(map(str, walk)) for walk in walks]
      model = Word2Vec(walks, vector_size=part_d, window=self.k, min_count=0, \
                       sg=1, workers=8, epochs=self.epochs)
      return model
      
   def get_embeddings(self, X):
      return [self.wv[x] for x in X]

   def fit(self, X, y):
      models = []
      part_size = int(self.d / self.partitions)
     
      G = self._read_graph()
      if type(self.p) is list:
          # create an embedding for each (p,q)
          for i in range(self.partitions):
             n2v_G = Node2Vec(G, self.directed, float(self.p[i]), \
                              float(self.q[i]), self.r, self.restarts, \
                              self.tau, self.omega, self.epsilon, self.s)
             n2v_G.preprocess_transition_probs()
             walks = n2v_G.simulate_walks(self.r, self.l)
             models.append(self._learn_embeddings(walks, part_size))

          self.wv = {}
         
          # concatenate the embeddings
          for key in models[0].wv.index_to_key:
             self.wv[key] = np.zeros(self.d, dtype=float)
             vect_size = 0
             for i in range(0, self.partitions):
                old_size = vect_size
                vect_size = part_size*(i+1)
               
                # fill in the array
                k = 0
                for j in range(old_size, vect_size):
                   self.wv[key][j] = models[i].wv[key][k]
                   k += 1
                #for j
             #for key
          #for i
          if self.dir_out is not None:
             with open(f"{self.dir_out}/{EMBEDDING_F_OUT_PKL}", 'wb') as f:
                pickle.dump(self.wv, f)
      else:
          self.node2vec = Node2Vec(G, self.directed, float(self.p), \
                                   float(self.q), self.r, self.restarts, \
                                   self.tau, self.omega, self.epsilon, self.s)
          self.node2vec.preprocess_transition_probs()
          walks = self.node2vec.simulate_walks(self.r, self.l)
          model = self._learn_embeddings(walks, self.d)
          self.wv = model.wv

          if self.dir_out is not None:
             self.wv.save(f"{self.dir_out}/{EMBEDDING_F_OUT}")

      X_embeddings = self.get_embeddings(X)
      self.clf = OneVsRestClassifier(SVC()).fit(X_embeddings, y)
      
      return self


   def predict(self, X):
      X_embeddings = self.get_embeddings(X)
      return self.clf.predict(X_embeddings)
