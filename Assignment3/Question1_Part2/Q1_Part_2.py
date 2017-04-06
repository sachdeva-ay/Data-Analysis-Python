
# coding: utf-8

# In[18]:

import pandas as pd


# In[19]:

df=pd.read_csv(r'vehicle_collisions.csv')


# In[20]:

df.BOROUGH.unique()


# In[21]:

df.BOROUGH.value_counts()


# In[22]:

df.sort_index()


# In[23]:

df_1=df.fillna(0)


# In[25]:

#Filling in the String values for every Vehicle type column by 1

df_1['VEHICLE 1 TYPE'] = df_1['VEHICLE 1 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')
df_1['VEHICLE 2 TYPE'] = df_1['VEHICLE 2 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')
df_1['VEHICLE 3 TYPE'] = df_1['VEHICLE 3 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')
df_1['VEHICLE 4 TYPE'] = df_1['VEHICLE 4 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')
df_1['VEHICLE 5 TYPE'] = df_1['VEHICLE 5 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')


# In[26]:

df_1


# In[27]:

#Replacing 0 where there are no values
df_2=df_1.fillna(0)


# In[49]:

#Grouped the dataset by BOROUGH
df_group=pd.DataFrame(df_2.groupby(['BOROUGH']).size().reset_index())
df_group=df_group[df_group.BOROUGH!=0]


# In[51]:

#Applying lamda function checked where for which borough how many vehicles were involved in the collision
df_group['One Vehicle Involved']=df_group['BOROUGH'].apply(lambda x: len(df_2[(df_2['BOROUGH']==x)
& (df_2['VEHICLE 1 TYPE']==1)& (df_2['VEHICLE 2 TYPE']==0) & (df_2['VEHICLE 3 TYPE']==0)
& (df_2['VEHICLE 4 TYPE']==0)& (df_2['VEHICLE 5 TYPE']==0)]))

df_group['Two Vehicle Involved']=df_group['BOROUGH'].apply(lambda x: len(df_2[(df_2['BOROUGH']==x)
& (df_2['VEHICLE 1 TYPE']==1)& (df_2['VEHICLE 2 TYPE']==1) & (df_2['VEHICLE 3 TYPE']==0)
& (df_2['VEHICLE 4 TYPE']==0)& (df_2['VEHICLE 5 TYPE']==0)]))

df_group['Three Vehicle Involved']=df_group['BOROUGH'].apply(lambda x: len(df_2[(df_2['BOROUGH']==x)
& (df_2['VEHICLE 1 TYPE']==1)& (df_2['VEHICLE 2 TYPE']==1) & (df_2['VEHICLE 3 TYPE']==1)
& (df_2['VEHICLE 4 TYPE']==0)& (df_2['VEHICLE 5 TYPE']==0)]))

df_group['Four or more Vehicles Involved']=df_group['BOROUGH'].apply(lambda x: len(df_2[(df_2['BOROUGH']==x)
& (df_2['VEHICLE 1 TYPE']==1)& (df_2['VEHICLE 2 TYPE']==1) & (df_2['VEHICLE 3 TYPE']==1)
& (df_2['VEHICLE 4 TYPE']==1)& (df_2['VEHICLE 5 TYPE']==1)]))


# In[52]:

df_group


# In[53]:

df_group.to_csv('Question1_Part2.csv')


# In[39]:

''''
df_2['VEHICLE 1 TYPE']=df_2['VEHICLE 1 TYPE'].astype(str).astype(int)
df_2['VEHICLE 2 TYPE']=df_2['VEHICLE 2 TYPE'].astype(str).astype(int)
df_2['VEHICLE 3 TYPE']=df_2['VEHICLE 3 TYPE'].astype(str).astype(int)
df_2['VEHICLE 4 TYPE']=df_2['VEHICLE 4 TYPE'].astype(str).astype(int)
df_2['VEHICLE 5 TYPE']=df_2['VEHICLE 5 TYPE'].astype(str).astype(int)

df_2['Sum'] = df_2['VEHICLE 1 TYPE'] + df_2['VEHICLE 2 TYPE'] + df_2['VEHICLE 3 TYPE']
            + df_2['VEHICLE 4 TYPE'] + df_2['VEHICLE 5 TYPE']

df_2['Sum']=df_2['Sum'].astype(str).astype(int)

df_new=df_2[['BOROUGH','Sum']]

df_result=df_new.groupby(['BOROUGH','Sum']).size().reset_index(name='count')

f=df_final.groupby('Sum')

result=pd.DataFrame(df_final.transpose())

result
''''

