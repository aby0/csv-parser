# Given source and destination cluster the data and filter csv
# =============================================================

import csv
import pandas as pd
import numpy as np

# Filter csv and return a dataframe
# ===================================


def filtercsv(file_name):

    data = pd.read_csv(file_name)

    data["_source_doj"] = pd.to_datetime(data["_source_doj"]).astype(np.int64)
    data["_source_timestamp"] = pd.to_datetime(data["_source_timestamp"]).astype(np.int64)

    data["_index"] = (data["_source_doj"] - data["_source_timestamp"])
    data.rename(columns={'_index': 'time_diff'}, inplace=True)

    return data

# Form a csv for specific source and destination
# ===============================================


def formcsv(src, des, data, file):
    temp_data = []
    columns = ['source_fare', 'time_diff']

    for index, rows in data.iterrows():
        temp = {}
        temp1 = rows.loc([((rows._source_source == src) & (rows._source_destination == des))])
        temp[0] = (temp1["_source_fare"])
        temp[1] = (temp1["time_diff"])
        temp_data.append(temp)

    with open(file, 'wb') as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(columns)
        j = 0
        for i in temp_data:
            csv_w.writerow(i.values())

data = filtercsv('file.csv')
formcsv('CCU', 'DEL', data, 'temp.csv')

temp_1 = pd.read_csv('temp.csv')

print data.shape
print temp_1.shape

