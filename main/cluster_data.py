# Given a csv file and number of cluster, this file will
# Cluster the data set
# ======================================================


from sklearn.cluster import KMeans
import pandas as pd


def cluster(file_name, n_cluster):

    data = pd.read_csv(file_name)
    data = data.as_matrix()
    y_pred = KMeans(n_clusters=n_cluster, random_state=10).fit_predict(data)
    return y_pred


