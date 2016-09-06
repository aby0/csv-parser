from lib import csv_parser
from lib import cluster_data
from lib import findcluster_kmeans
from lib import model_data
from lib.util import realpath
import numpy as np


def cluster_data_route(source, destination, fare_class, data):

    PRICING_JSON = realpath('../dataset/pricing.2016-09-01.json')
    PRICING_CSV = realpath('../dataset/pricing.2016-09-01.csv')
    ROUTE_CSV = realpath('../dataset/' + source + "_" + destination + ".csv")

    if data is None:
        csv_parser.parsejson(PRICING_JSON, PRICING_CSV)
        print "Parsed Data."

        data = model_data.filtercsv(PRICING_CSV)
        print "Modelled Data."

    model_data.formcsv(source, destination, data, fare_class, ROUTE_CSV)
    print "Created Route CSV."

    cluster_num = findcluster_kmeans.calculatecluster(ROUTE_CSV)
    if cluster_num == -1:
        return [None, None]
    print("Ideal #cluster : "+str(cluster_num))

    cluster_centroid, price_ranges = cluster_data.cluster(ROUTE_CSV, cluster_num)

    np.set_printoptions(precision=3, suppress=True)
    cluster_centroid = np.asarray(cluster_centroid)
    sorted_cluster_centroid = sorted(cluster_centroid[:, 0])

    print(sorted_cluster_centroid)
    return [sorted_cluster_centroid, price_ranges]

if __name__ == '__main__':
    source = "BLR"
    destination = "DEL"
    fare_class = "E"
    cluster_data_route(source, destination, fare_class, None)
