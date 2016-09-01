from lib import csv_parser
from lib import cluster_data
from lib import findcluster_kmeans
from lib import model_data
from lib.util import realpath
import numpy as np

PRICING_JSON = realpath('../dataset/pricing.2016-09-01.json')
PRICING_CSV = realpath('../dataset/pricing.2016-09-01.csv')
DEL_CCU_CSV = realpath('../dataset/DEL_CCU.csv')
csv_parser.parsejson(PRICING_JSON, PRICING_CSV)
data = model_data.filtercsv(PRICING_CSV)
model_data.formcsv('DEL', 'CCU', data, 'E', DEL_CCU_CSV)

cluster_num = findcluster_kmeans.calculatecluster(DEL_CCU_CSV)
cluster_centroid = cluster_data.cluster(DEL_CCU_CSV, cluster_num)
# Check cluster_centroid

if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    cluster_centroid = np.asarray(cluster_centroid)
    print(cluster_centroid[:, 0])
    print(cluster_num)

