import csv
import matplotlib
import pandas as pd
import sklearn
data = pd.read_csv('data.csv')

# print data.head(2)
# Manipulate the time difference between doj and search timestamp
data["_source_doj"] = pd.to_datetime(data["_source_doj"])
data["_source_timestamp"] = pd.to_datetime(data["_source_timestamp"])

data["_index"] = data["_source_doj"] - data["_source_timestamp"]
data.rename(columns={'_index': 'time_diff'}, inplace=True)

#Form a csv for specific source and destination

def formCsv(src, des, data, file):
    temp_data = []
    columns = ['source_fare', 'time_diff']


    for index, rows in data.iterrows():
        temp = {}
        # print rows
        # break
        temp1 = rows.loc([((rows._source_source == src) & (rows._source_destination == des))])
        # print temp1
        temp[0] = (temp1["_source_fare"])
        temp[1] = (temp1["time_diff"])
        temp_data.append(temp)

    with open(file, 'wb') as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(columns)
        for i in temp_data:
            csv_w.writerow(i.values())


# src = "CCU"
# des = "BOM"
#
# name = src+'_' + des + '.csv'

#
# formCsv(src, des, data, name)


# Find all unique flight_id and time_diff and plot it

#Do the clustering and find optimum number of cluster to take into account

# print data.head(1)
# print data["_index"]
# print data["_source_doj"]
# print data["_source_timestamp"]
