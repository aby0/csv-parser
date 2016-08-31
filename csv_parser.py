import json
import csv

# Flatten the json


def flattenjson( b, delim ):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]

    return val


f = open('pricing.2016-08-30.json')
flat = []
for line in f:
    # print line
    data = json.loads(line)
    flat.append(flattenjson(data, "_"))
    # print flat
f.close()

columns = {}
columns = list(set(flat[0].keys()))
print columns

with open('data.csv', 'wb') as out_file:
    csv_w = csv.writer(out_file)
    csv_w.writerow(columns)
    for i in flat:
        csv_w.writerow(i.values())




