# Given a csv file and number of cluster, this file will
# Cluster the data set
# ======================================================


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd


def cluster(file_name, n_cluster):

    data = pd.read_csv(file_name)
    data = data.as_matrix()
    clusterer = KMeans(n_clusters=n_cluster, random_state=10)
    y_pred = clusterer.fit_predict(data)
    plt.scatter(data[:, 0], data[:, 1], c=y_pred)
    plt.show()
    return clusterer.cluster_centers_


