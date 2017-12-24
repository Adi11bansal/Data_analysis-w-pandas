import quandl
import pandas as pd

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()

df = quandl.get("FMAC/HPI_TX", authtoken=api_key)

#print(df.head())


fiddy_states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states[0][0])


