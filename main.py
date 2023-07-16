# Importing libraries
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def sqr_dist(a, b):  # Function for Distance
    return ((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2)


# Extracting dataset
with open('dataset.json') as a:
    ds = json.load(a)
a = np.array(ds['red'] + ds['blue'])
df = pd.DataFrame(a, columns=['x', 'y'])
print(df)
xes = np.array(df['x'])
yes = np.array(df['y'])

# Randomly initializing cluster centroids
k1 = np.random.randint(low=-50, high=50, size=(2,))
k2 = np.random.randint(low=-50, high=50, size=(2,))
print("Initial K1",k1)
print("Initial K2",k2)

# Initial plot
plt.scatter(xes, yes, color='gray', label='Dataset')
plt.scatter(k1[0], k1[1], marker='x', color='orange', label='Initial K1')
plt.scatter(k2[0], k2[1], marker='D', color='green', label='Initial K2')

# Main logic
k1s = []
k2s = []
for i in range(150):  # 150 cycles of loop
    k1s = []
    k2s = []
    for j in a:
        if sqr_dist(j, k1) >= sqr_dist(j, k2):  # Assigning the dataset to cluster centroids
            k2s.append(j)
        else:
            k1s.append(j)

    k1 = np.sum(np.array(k1s), axis=0) / len(k1s)
    k2 = np.sum(np.array(k2s), axis=0) / len(k1s)

print("Final k1", k1)
print("Final k2", k2)
plt.scatter(k1[0], k1[1], marker='x', color='red', label='Final K1')
plt.scatter(k2[0], k2[1], marker='D', color='blue', label='Final K2')
plt.legend()
plt.savefig("fig.png")
plt.show()
