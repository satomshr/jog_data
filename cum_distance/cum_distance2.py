# cum_distance2.py ; draw graph of cumulative distance of each year
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

data = pd.read_csv('..\\data\\total_data.csv')
data = data[ data[data.columns[2]] == 'Run'] # 'Run' only

data[data.columns[1]] = pd.to_datetime(data[data.columns[1]]) # convert to datetime64[ns]
data = data.sort_values(data.columns[1])

data_2018 = data[ data[data.columns[1]] < '2019-01-01' ]
data_2019 = data[ data[data.columns[1]] < '2020-01-01' ]
data_2019 = data_2019[ data_2019[data_2019.columns[1]] >= '2019-01-01' ]
data_2020 = data[ data[data.columns[1]] < '2021-01-01' ]
data_2020 = data_2020[ data_2020[data_2020.columns[1]] >= '2020-01-01' ]


def year_to_2020(x):
    return datetime.datetime(2020, x.month, x.day)


x_2018 = data_2018[data_2018.columns[1]].map(year_to_2020)
y_2018 = data_2018[data_2018.columns[6]].cumsum()
x_2019 = data_2019[data_2019.columns[1]].map(year_to_2020)
y_2019 = data_2019[data_2019.columns[6]].cumsum()
x_2020 = data_2020[data_2020.columns[1]]
y_2020 = data_2020[data_2020.columns[6]].cumsum()

ymin = 0
ymax = 1600

plt.plot(x_2018, y_2018, "y-", label="2018")
plt.plot(x_2019, y_2019, "r-", label="2019")
plt.plot(x_2020, y_2020, "b-", label="2020")
plt.xlabel("Month")
plt.xlim(datetime.datetime(2020, 1, 1), datetime.datetime(2021, 1, 1))
plt.ylabel("Cumulative distance (km)")
plt.ylim(ymin, ymax)
plt.grid(True)
plt.legend(loc="upper left")

# http://hydro.iis.u-tokyo.ac.jp/~ikeuchi/it-memo/python/python-mpl.html
datefmt = mdates.DateFormatter('%m')
plt.gca().xaxis.set_major_formatter(datefmt)

plt.savefig("cum_distance2.svg")
