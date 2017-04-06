
# coding: utf-8

# In[1]:

import pandas as pd
df=pd.read_csv(r'cricket_matches.csv')


# In[2]:

#if the home time is the winning team then place it in the output_team column else NaN
import numpy as np
df['output_team'] = np.where((df['home'] == df['winner']), df['home'], np.nan)


# In[3]:

#taking only results where the home team is the winner and placing in a new dataset
df_1=df[df.home==df.winner]


# In[4]:

#to check which were the innings played by the home team
df_1["Score"] = np.where((df_1['innings1']==df_1['winner']), df_1['innings1_runs'], df_1['innings2_runs'])


# In[5]:

#Calculating the Avg Score of the home team
home_team_avg=pd.DataFrame(df_1.groupby('home').Score.mean())


# In[6]:

home_team_avg.head()


# In[7]:

home_team_avg.to_csv('Question3_Part1_Cricket.csv')

