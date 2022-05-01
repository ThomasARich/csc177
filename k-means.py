import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import cluster
import matplotlib.pyplot as plt

dataset = pd.read_csv('imdb_dataset.csv')

# Split into x and y data. Perform train-test split.
x = dataset['title']
y = dataset[['critics_score', 'audience_score']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, shuffle=True) # 70% training and 30% test

# Cluster data for calculation of k-mean.
k_means = cluster.KMeans(n_clusters=6, max_iter=50, random_state=1)
k_means.fit(y_test) 
labels = k_means.labels_
labl = pd.DataFrame(labels, index=x_test, columns=['Cluster ID'])

centroids = k_means.cluster_centers_
centr = pd.DataFrame(centroids,columns=y_test.columns)

print(labl)
print(centr)

# Plot SSE vs # of K-Means.
numClusters = [1,2,3,4,5,6]
SSE = []
for k in numClusters:
    k_means = cluster.KMeans(n_clusters=k)
    k_means.fit(y_test)
    SSE.append((k_means.inertia_)*.0001) # simplifying dataset.

plt.plot(numClusters, SSE)
plt.xlabel('Number of Clusters')
plt.ylabel('SSE')

plt.savefig('sse_cluster.png')