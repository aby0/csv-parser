# Given source and destination cluster the data and filter csv
# =============================================================

import csv
import pandas as pd
import numpy as np

# Filter csv and return a dataframe
# ===================================


def filtercsv(file_name):

    data = pd.read_csv(file_name)

    data["_source_doj"] = pd.to_datetime(data["_source_doj"])
    data["_source_timestamp"] = pd.to_datetime(data["_source_timestamp"])

    data["_index"] = (data["_source_doj"] - data["_source_timestamp"])
    data["_index"] = data["_index"].astype('timedelta64[D]')
    data.rename(columns={'_index': 'time_diff'}, inplace=True)

    return data

# Form a csv for specific source and destination
# ===============================================


def formcsv(src, des, data, fare_class, file):
    temp_data = []
    columns = ['source_fare', 'time_diff']
    data = data[((data._source_source == src) & (data._source_destination == des) &
                 (data._source_fare_class == fare_class))]

    for index, rows in data.iterrows():
        temp = {}
        temp1 = rows.loc()
        temp[0] = (temp1["_source_fare"])
        temp[1] = (temp1["time_diff"])
        temp_data.append(temp)

    with open(file, 'wb') as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(columns)
        j = 0
        for i in temp_data:
            csv_w.writerow(i.values())



