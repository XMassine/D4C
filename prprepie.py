import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import numpy as np



df=pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
df.set_index('Country', inplace=True)

years=list(map(str,range(1980,2014)))


dfjapan=df.loc['Japan',years]

dfjapan.plot(kind='box')
plt.show()

dfConti=df.groupby('Continent', axis=0).sum()

Color=['red', 'orange','yellow', 'green', 'blue', 'purple']
Explode=[0,0,0,0.1,0.1,0.1]

dfConti['Total'].plot(kind='pie', figsize=(10,6), explode=Explode, colors=Color, autopct='%1.1f%%', shadow=True, labels=None, pctdistance=1.2, startangle=90)
plt.legend(labels=dfConti.index, loc='upper left',fontsize=7)

plt.show()




