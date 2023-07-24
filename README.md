# K-means Algorithm Implementation

This repository contains an implementation of the K-means algorithm using Python, NumPy, Matplotlib, and Pandas. The
K-means algorithm is an unsupervised machine learning algorithm used for clustering data points into K distinct
clusters.

## Prerequisites

To run the code, you need the following dependencies installed:

- Python (version 3.6 or higher)
- NumPy
- Matplotlib
- Pandas

You can install the dependencies using pip:

```bash
pip install numpy matplotlib pandas
```
# Theory
The K-means algorithm is an unsupervised machine learning technique for clustering data points into K distinct groups. It starts by randomly placing K centroids in the feature space and then iteratively assigns each data point to the cluster with the closest centroid. After each assignment, the centroids are updated based on the mean of the data points in each cluster. This process continues until convergence, resulting in K clusters where each cluster represents similar data points. K-means is widely used for tasks like customer segmentation and image compression.
![Figure for K-Means Algorithm](https://raw.githubusercontent.com/jacksparrow404/k-means/main/fig.png)
# Getting Started
1. Clone the repository
```
git clone https://github.com/jacksparrow404/k-means
cd k-means
```
2. Run the 'main.py' script:
```
python main.py
```
3.The script will generate a scatter plot of the dataset along with the initial and final positions of the cluster centroids. The resulting plot will be saved as `fig.png` in the current directory.
# Customization
You can customize the code and experiment with different configurations:
* Adjust the number of iterations by changing the value in the `range()` function within the `for` loop.
* Customize the colors and markers used for the scatter plot and centroids in the `plt.scatter()` function calls.
* Modify the file name and format of the resulting plot by changing the argument in the `plt.savefig()` function.
* Modify the dataset by changing the values.

