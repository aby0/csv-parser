# This file parses a json into required csv format
# ==================================================

import json
import csv

# Helper function to flatten_json object
# ========================================


def flattenjson(b, delim):
    val = {}
    for i in b.keys():
        if isinstance(b[i], dict):
            get = flattenjson(b[i], delim)
            for j in get.keys():
                val[i + delim + j] = get[j]
        else:
            val[i] = b[i]

    return val

# Function to parse json object and create a new csv file
# =========================================================


def parsejson(file_json, file_csv):

    f = open(file_json)
    flat = []
    for line in f:
        data = json.loads(line)
        flat.append(flattenjson(data, "_"))
    f.close()

    columns = list(set(flat[0].keys()))

    with open(file_csv, 'wb') as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(columns)
        for i in flat:
            csv_w.writerow(i.values())


parsejson('dataset-json/pricing.2016-08-30.json', 'file.csv')

