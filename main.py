import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from copy import deepcopy

# read dataset
with open('dataset.json') as a:
    ds = json.load(a)
dataset = np.array(ds['red'] + ds['blue'])
clusters = int(input("Enter the number of clusters: "))
random_indices = np.random.choice(len(dataset), clusters, replace=False)
ks = dataset[random_indices]
initial_ks = deepcopy(ks)
cluster_centroids = []
print("Initial cluster centroids:",initial_ks)

# function for assigning the nearest points
def nearest(clusters, data):
    distances = list(map(np.linalg.norm, data-clusters))
    return np.argmin(distances)


# main loop
for i in range(100):
    assigned = {k: [] for k in range(clusters)}
    ds = deepcopy(ks)
    cluster_centroids.append(ds)
    for data in dataset:
        pos = nearest(ks, data)
        assigned[pos].append(data)
    for _ in range(clusters):
        ks[_] = np.mean(assigned[_], axis=0)


# Reassigning points for making points graph-ready
assigned_final = {k: [] for k in range(clusters)}
count = 1
for d in dataset:
    p = nearest(ks, d)
    assigned_final[p].append(d)
    count += 1


# Plotting and data visualization
cluster_centroids = np.array(cluster_centroids)
for i in range(clusters):
    plt.plot(cluster_centroids[:, i][:, 0],
             cluster_centroids[:, i][:, 1], color='gray', marker='*', zorder=0)
for a_ in assigned_final:
    plt.scatter(np.array(assigned_final[a_])[:, 0],
                np.array(assigned_final[a_])[:, 1], zorder=1)
plt.scatter(initial_ks[:, 0], initial_ks[:, 1],
            marker='x', zorder=2, label='Initial Centroids', color='black')
plt.scatter(ks[:, 0], ks[:, 1], marker='D', zorder=2,
            label='Final Centroids', color='black')
print("The final cluster centroids are: ", ks)


plt.legend()
plt.savefig('fig.png')
plt.show()
