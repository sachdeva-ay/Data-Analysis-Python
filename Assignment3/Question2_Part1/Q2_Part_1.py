
# coding: utf-8

# In[27]:

import pandas as pd


# In[28]:

#reading the csv file
df=pd.read_csv(r'employee_compensation.csv')


# In[29]:

#rename the total compensation column
df_1=df.rename(columns = {'Total Compensation':'Total_Compensation'})


# In[33]:

#grouping the data according to Organization Group and dedpartment having the highest average total compensation
df_group=pd.DataFrame(df_1.groupby(['Organization Group','Department']).Total_Compensation.mean())


# In[34]:

df_group.head()


# In[36]:

df_group.to_csv('Question2_Part1.csv')


# In[ ]:



