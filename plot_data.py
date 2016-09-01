import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('DEL_BOM.csv')
#data = data[(data.time_diff < 30) & (data.source_fare < 20000)]
p = data.plot.scatter(x='time_diff', y='source_fare')
plt.show()
