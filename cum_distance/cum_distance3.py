# cum_distance3.py ; draw graph of cumulative distance of each year
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

data = pd.read_csv('..\\data\\total_data.csv')
data = data[ data[data.columns[2]] == 'Run'] # 'Run' only

data[data.columns[1]] = pd.to_datetime(data[data.columns[1]]) # convert to datetime64[ns]
data = data.sort_values(data.columns[1])

year_min = data[data.columns[1]].min().year
year_max = data[data.columns[1]].max().year

def year_to_2020(x):
    return datetime.datetime(2020, x.month, x.day)

for y in range(year_min, year_max + 1):
    data_run = data[ data[data.columns[1]] >= str(y) + '-01-01']
    data_run = data_run[ data_run[data_run.columns[1]] < str(y+1) + '-01-01']
    plt.plot(
        data_run[ data_run.columns[1] ].map(year_to_2020),
        data_run[ data_run.columns[6] ].cumsum(),
        label=str(y)
    )
    print('CY{} ; {:8.3f} km'.format(y, data_run[ data_run.columns[6] ].sum()))

ymin = 0
ymax = 1800

plt.xlabel("Month")
plt.xlim(datetime.datetime(2020, 1, 1), datetime.datetime(2021, 1, 1))
plt.ylabel("Cumulative distance (km)")
plt.ylim(ymin, ymax)
plt.grid(True)
plt.legend(loc="upper left")
plt.title(label="updated on {0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()), loc="right")

# http://hydro.iis.u-tokyo.ac.jp/~ikeuchi/it-memo/python/python-mpl.html
datefmt = mdates.DateFormatter('%m')
plt.gca().xaxis.set_major_formatter(datefmt)

plt.savefig("cum_distance3.svg")
