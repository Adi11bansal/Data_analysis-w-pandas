import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats={'Day':[1,2,3,4,5,6],
           'Visitors':[34,45,23,12,55,23],
           'Bounce_Rate':[23,45,23,12,34,23]}


df=pd.DataFrame(web_stats)

#print(df)
#print(df.head())
#print(df.tail())
#print(df.head(2))



#print(df.set_index('Day'))
#print(df.head())


#df2=df.set_index('Day')
#print(df2.head())
#df.set_index('Day',inplace=True)
#print(df.head())



#print(df['Bounce Rate'])

#print(df.visitors)

#print(df[['Bounce_Rate','Visitors']])

print(df.Visitors.tolist())
print(np.array(df[['Bounce_Rate','Visitors']]))
df2=pd.DataFrame(np.array(df[['Bounce_Rate','Visitors']]))
print(df2)
