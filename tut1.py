import pandas as pd
import datetime
from pandas.io import data, web # becomes
from pandas_datareader import data, web
start = datatime.datetime(2010,1,1)
end=endtime.datetime(2015,8,22)
df=web.DataReader("XOM","yahoo",start,end)
print(df.head())
