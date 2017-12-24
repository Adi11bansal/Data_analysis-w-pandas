import pandas as pd

df=pd.read_csv('C:\Python35\datanalysis/yuio.csv')

print(df.head(10))

df.set_index('Date',inplace=True)
df.to_csv('new2.csv')

df=pd.read_csv('C:\Python35\datanalysis/new2.csv')
print(df.head())


df=pd.read_csv('C:\Python35\datanalysis/new2.csv',index_col=0)
print(df.head())



df.columns =['Austin']
print(df.head())
df.to_csv('new3.csv')
df.to_csv('new4.csv',header=False)




df=pd.read_csv('C:\Python35\datanalysis/new4.csv',names=['Date','Austin'],index_col=0)
print(df.head())

df.to_html('exm.html')

df=pd.read_csv('C:\Python35\datanalysis/new4.csv',names=['Date','Austin'])
print(df.head())

df.rename(columns={'Austin':'77006'},inplace=True)
print(df.head())

