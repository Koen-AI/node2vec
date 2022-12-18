import matplotlib.pyplot as plt
import pickle
import numpy as np

# https://scikit-optimize.github.io/stable/modules/generated/skopt.BayesSearchCV.html

CMAP = "viridis"

def plot_heatmap(DIR, restarts):
   with open(f"{DIR}/opt_results.pkl", 'rb') as f:
      data = pickle.load(f)
   
   # Scores per hyperparameter configuration
   scores = data["mean_test_score"]
   best_score = np.argmax(scores)

   fig, ax = plt.subplots()
   
   if restarts:
       # Obtain hyperparameter configurations
       omega, tau = [], []
       for item in data["params"]:
          omega.append(item["omega"])
          tau.append(item["tau"])

       ax.plot(omega, tau, "ko", markersize=2)
       ax.plot(omega[best_score], tau[best_score], markersize=6, marker='*', color='red')
       cntr = ax.tricontourf(omega, tau, scores, cmap=CMAP)
       
       ax.set(
          xlim=(min(omega), max(omega)),
          ylim=(min(tau), max(tau)),
          xlabel=r"$\omega$",
          ylabel=r"$\tau$"
       )
   else:
       # Obtain hyperparameter configurations
       p, q = [], []
       for item in data["params"]:
          p.append(item["p"])
          q.append(item["q"])

       ax.plot(p, q, "ko", markersize=2)
       ax.plot(p[best_score], q[best_score], markersize=6, marker='*', color='red')
       cntr = ax.tricontourf(p, q, scores, cmap=CMAP)
       
       ax.set(
          xlim=(min(p), max(p)),
          ylim=(min(q), max(q)),
          xlabel=r"$p$",
          ylabel=r"$q$"
       )
   fig.colorbar(cntr, ax=ax, label="F1-macro score")
   plt.savefig(bbox_inches="tight", fname=f"{DIR}/BO_opt.pdf", format="pdf", dpi=100)
