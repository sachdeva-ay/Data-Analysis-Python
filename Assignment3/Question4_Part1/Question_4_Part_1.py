
# coding: utf-8

# In[1]:

# Importing all the libraries
import pandas as pd
from pandas import DataFrame
import numpy as np
import calendar


# In[3]:

# Reading the csv file
df=pd.read_csv(r'movies_awards.csv')


# In[4]:

#extracting the wins and nominations according to the awards in their respective columns
df['Awards_Won'] = df['Awards'].str.extract('(\d+) win', expand=True)
df['Awards_Nominated'] = df['Awards'].str.extract('(\d+) nomination', expand=True)
df['PrimeAwards_Won']= df['Awards'].str.extract('Won (\d+) Primetime', expand=True)
df['PrimeAwards_Nominations']= df['Awards'].str.extract('Nominated for (\d+) Primetime', expand=True)
df['BaftaAwards_Won']= df['Awards'].str.extract('Won (\d+) BAFTA', expand=True)
df['BaftaAwards_Nominations']= df['Awards'].str.extract('Nominated for (\d+) BAFTA', expand=True)
df['OscarAwards_Won']= df['Awards'].str.extract('Won (\d+) Oscar', expand=True)
df['OscarAwards_Nominations']= df['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True)
df['GoldenGlobeAwards_Won']= df['Awards'].str.extract('Won (\d+) Golden Globe', expand=True)
df['GoldenGlobeAwards_Nominations']= df['Awards'].str.extract('Nominated for (\d+) Golden Globe', expand=True)


# In[5]:

#keping only the columns needed for the result
df_1=df[[15,21,22,23,24,25,26,27,28,29,30]]


# In[6]:

result = df_1.fillna(0)


# In[7]:

result


# In[11]:

#converting pandas objects to int
result['Awards_Won'] = result['Awards_Won'].astype(str).astype(int)
result['PrimeAwards_Won'] = result['PrimeAwards_Won'].astype(str).astype(int)
result['BaftaAwards_Won']=result['BaftaAwards_Won'].astype(str).astype(int) 
result['OscarAwards_Won']=result['OscarAwards_Won'].astype(str).astype(int) 
result['GoldenGlobeAwards_Won']=result['GoldenGlobeAwards_Won'].astype(str).astype(int)


# In[12]:

result['Awards_Nominated'] =result['Awards_Nominated'].astype(str).astype(int) 
result['PrimeAwards_Nominations']=result['PrimeAwards_Nominations'].astype(str).astype(int)
result['BaftaAwards_Nominations']=result['BaftaAwards_Nominations'].astype(str).astype(int)
result['OscarAwards_Nominations']=result['OscarAwards_Nominations'].astype(str).astype(int)  
result['GoldenGlobeAwards_Nominations']=result['GoldenGlobeAwards_Nominations'].astype(str).astype(int)


# In[13]:

#Totalling up the awards won by each movie
result['Awards_Won'] = result['Awards_Won']+result['PrimeAwards_Won']+result['BaftaAwards_Won']+result['OscarAwards_Won']+result['GoldenGlobeAwards_Won']


# In[17]:

#Calculating the no of times the movie has been nominated for awards
result['Awards_Nominated']=result['Awards_Nominated']+result['PrimeAwards_Nominations']+result['BaftaAwards_Nominations']+result['OscarAwards_Nominations']+result['GoldenGlobeAwards_Nominations']


# In[19]:

result.head()


# In[15]:

result.to_csv('Question4_Part1.csv')

