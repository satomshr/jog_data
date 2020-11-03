# cum_distance.py ; draw graph of cumulative distance of each year
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv('..\\data\\total_data.csv')
data[data.columns[1]] = pd.to_datetime(data[data.columns[1]]) # convert to datetime64[ns]
data = data.sort_values(data.columns[1])

data_2018 = data[ data[data.columns[1]] < '2019-01-01' ]
data_2019 = data[ data[data.columns[1]] < '2020-01-01' ]
data_2019 = data_2019[ data_2019[data_2019.columns[1]] >= '2019-01-01' ]
data_2020 = data[ data[data.columns[1]] < '2021-01-01' ]
data_2020 = data_2020[ data_2020[data_2020.columns[1]] >= '2020-01-01' ]

# plots
# x_2018 = data_2018[data_2018.columns[1]]
# y_2018 = data_2018[data_2018.columns[6]].cumsum()
# plt.plot(x_2018, y_2018)

x_2019 = data_2019[data_2019.columns[1]]
y_2019 = data_2019[data_2019.columns[6]].cumsum()
x_2020 = data_2020[data_2020.columns[1]]
y_2020 = data_2020[data_2020.columns[6]].cumsum()

ymin = 0
ymax = 1600

figure, (Left, Right) = plt.subplots(ncols=2, figsize=(20, 10))
Left.plot(x_2019, y_2019)
Left.set_title("CY2019")
Left.set_ylabel("Cumulative distance(km)")
Left.set_xlim(datetime.datetime(2019, 1, 1), datetime.datetime(2020, 1, 1))
Left.set_ylim(ymin, ymax)
Left.grid(True)

Right.plot(x_2020, y_2020)
Right.set_title("CY2020")
Right.set_ylabel("Cumulative distance(km)")
Right.set_xlim(datetime.datetime(2020, 1, 1), datetime.datetime(2021, 1, 1))
Right.set_ylim(ymin, ymax)
Right.grid(True)

# figure.show()
figure.savefig("cum_distance.svg")
