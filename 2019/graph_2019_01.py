# graph_2019_91.py ; draw graph of 2019.csv
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("2019.csv")
x = pd.to_datetime(data[data.columns[1]]) # Date, convert to datetime64[ns]
y = data[data.columns[6]] # Distance [km]

# plot
plt.plot(x, y.cumsum()) # cumulative summation

# x-axis range
# sxmin = '2019-01-01'
# sxmax = '2019-12-31'
# xmin = datetime.datetime.strptime(sxmin, '%Y-%m-%d')
# xmax = datetime.datetime.strptime(sxmax, '%Y-%m-%d')
# plt.xlim([sxmin, sxmax])
plt.ylim([0, 1300])

# plt.xticks(rotation=90)
plt.grid(True)

plt.title("Cumulative Jogging Distance of CY2019")
plt.xlabel("Date")
plt.ylabel("Cumulative distance(km)")

# plt.show()
plt.savefig("2019.svg")
