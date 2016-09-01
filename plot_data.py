import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('BLR_VTZ.csv')
data = data[(data.time_diff < 3) & (data.source_fare < 20000)]
p = data.plot.scatter(x='source_fare', y='time_diff')
plt.show()
