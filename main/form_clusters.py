from lib import csv_parser
from lib import cluster_data
from lib import findcluster_kmeans
from lib import model_data

csv_parser.parsejson('pricing.2016-09-01.json', 'pricing.2016-09-01.csv')
data = model_data.filtercsv('pricing.2016-09-01.csv')
model_data.formcsv('CCU', 'BLR', data, 'E', 'CCU_BLR.csv')

cluster_num = findcluster_kmeans.calculatecluster('CCU_BLR.csv')
cluster_centroid = cluster_data.cluster('CCU_BLR.csv', cluster_num)
# Check cluster_centroid

print cluster_centroid