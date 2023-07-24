import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from copy import deepcopy

with open('dataset.json') as a:
    ds = json.load(a)
dataset = np.array(ds['red'] + ds['blue'])
clusters = int(input("Enter the number of clusters: "))

random_indices = np.random.choice(len(dataset), clusters, replace=False)
ks = dataset[random_indices]
initial_ks = deepcopy(ks)


cluster_centroids = []


def nearest(clusters, data):
    distances = list(map(np.linalg.norm, data-clusters))
    return np.argmin(distances)


for i in range(20):
    assigned = {k: [] for k in range(clusters)}
    ds = deepcopy(ks)
    cluster_centroids.append(ds)
    for data in dataset:
        pos = nearest(ks, data)
        assigned[pos].append(data)
    for _ in range(clusters):
        ks[_] = np.mean(assigned[_], axis=0)


# Plotting
cluster_centroids = np.array(cluster_centroids)
for i in range(clusters):
    plt.plot(cluster_centroids[:, i][:, 0],
             cluster_centroids[:, i][:, 1], color='gray', marker='*')
for a_ in assigned:
    plt.scatter(np.array(assigned[a_])[:, 0], np.array(assigned[a_])[:, 1])
for k1 in initial_ks:
    plt.scatter(k1[0], k1[1], marker='x')
for k_ in ks:
    plt.scatter(k_[0], k_[1], marker='D')

print("The final cluster centroids are: ", ks)
plt.savefig('fig.png')
plt.show()
