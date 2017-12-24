import pandas as pd
df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

##merged=pd.merge(df1,df3,on='Year',how='inner')
##merged=pd.merge(df1,df3,on='Year',how='outer')
##merged=pd.merge(df1,df3,on='Year',how='left')
merged=pd.merge(df1,df3,on='Year',how='right')
merged.set_index(['Year','Int_rate'],inplace=True)
print(merged)

