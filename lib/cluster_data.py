# Given a csv file and number of cluster, this file will
# Cluster the data set
# ======================================================


from sklearn.cluster import KMeans
from lib.util import realpath
import pandas as pd
import matplotlib.pyplot as plt


def cluster(file_name, n_cluster):

    data = pd.read_csv(file_name)
    data = data[(data.time_diff >= 0)]
    data = data.as_matrix()
    clusterer = KMeans(n_clusters=n_cluster, random_state=10)
    y_pred = clusterer.fit_predict(data)
    clustered_data = {}
    counter = 0
    for i in y_pred:
        index = str(i)
        if index in clustered_data:
            clustered_data[index].append(data[counter][0])
        else:
            clustered_data[index] = [data[counter][0]]
        counter += 1


    price_ranges = []
    for i in clustered_data:
        arr = clustered_data[i]
        price_ranges.append((min(arr), max(arr)))

    price_ranges = sorted(price_ranges)
    print price_ranges

    # title_data = file_name.split("/")
    # title_data = title_data[len(title_data) - 1]
    # title = title_data.split(".")[0]
    # plt.scatter(data[:, 1], data[:, 0], c=y_pred)
    # plt.title(title)
    # img_path = realpath('../images/' + title)
    # plt.savefig(img_path)
    # plt.clf()
    # plt.cla()
    return [clusterer.cluster_centers_, price_ranges]

if __name__=='__main__':
    source = "BLR"
    destination = "DEL"
    fare_class = "E"
    ROUTE_CSV = realpath('../dataset/' + source + "_" + destination + ".csv")
    cluster(ROUTE_CSV, 4)