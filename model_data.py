import csv
import pandas as pd
data = pd.read_csv('data.csv')

# print data.head(2)
# Manipulate the time difference between doj and search timestamp
data["_source_doj"] = pd.to_datetime(data["_source_doj"])
data["_source_timestamp"] = pd.to_datetime(data["_source_timestamp"])

data["_index"] = data["_source_doj"] - data["_source_timestamp"]
data["_index"] = data["_index"].astype('timedelta64[D]')
data.rename(columns={'_index': 'time_diff'}, inplace=True)

#Form a csv for specific source and destination

def formCsv(src, des,fare_class, data, file):
    temp_data = []
    columns = ['source_fare', 'time_diff']

    data = data[((data._source_source == src) & (data._source_destination == des) & (data._source_fare_class == fare_class))]

    for index, rows in data.iterrows():
        temp = {}
        # print rows
        # break
        temp1 = rows.loc()
        temp[0] = (temp1["_source_fare"])
        temp[1] = (temp1["time_diff"])
        temp_data.append(temp)

    with open(file, 'wb') as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(columns)
        for i in temp_data:
            csv_w.writerow(i.values())


src = "DEL"
des = "BLR"
fare_class = "E"

name = src+'_' + des + '.csv'


formCsv(src, des,fare_class, data, name)


# Find all unique flight_id and time_diff and plot it

#Do the clustering and find optimum number of cluster to take into account

# print data.head(1)
# print data["_index"]
# print data["_source_doj"]
# print data["_source_timestamp"]
