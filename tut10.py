import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]



def grab_intial_state_data():
    states=state_list()
    main_df = pd.DataFrame()
    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        print(query)
        df = quandl.get(query, authtoken=api_key)
        df.columns=[str(abbv)]
        df[abbv]=(df[abbv]-df[abbv][0])/df[abbv][0]*100.0 

        if main_df.empty:
            main_df = df
        else:
            main_df = pd.merge(main_df, df, right_index=True, left_index=True)
        print(main_df.head())



    pickle_out=open('fiddy_states3.pickle','wb')
    pickle.dump(main_df,pickle_out)
    pickle_out.close()

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    return df
    

#grab_intial_state_data()


fig = plt.figure()
ax1=plt.subplot2grid((1,1),(0,0))
HPI_data = pd.read_pickle('fiddy_states3.pickle')
HPI_data['AL1yr'] = HPI_data['AL'].resample('A',how='mean')
#AL1yr = HPI_data['AL'].resample('A',how='mean')
print(HPI_data[['AL','AL1yr']].head())
##HPI_data.dropna(how='all',inplace=True)
HPI_data.fillna(value=-99999,limit=10,inplace=True)
print(HPI_data[['AL','AL1yr']].head())

#print(HPI_data.isnull().values.sum())

HPI_data[['AL','AL1yr']].plot(ax = ax1)
plt.legend(loc=4)
plt.show()

