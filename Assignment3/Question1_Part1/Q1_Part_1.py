
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

#reading the csv in dataframe
df=pd.read_csv(r'vehicle_collisions.csv')


# In[22]:

#converting the data object to datatime 
df['DATE'] = pd.to_datetime(df['DATE'], coerce=True)


# In[23]:

#extracting the month from the Date column
df['Month']=df['DATE'].dt.strftime('%B')


# In[27]:

df.head()


# In[26]:

#df['Year'] = df['DATE'].apply(lambda x:x.split('/')[2])
#df.Year.unique()
#df['Month'] = df['DATE'].apply(lambda x:x.split('/')[0])

#taking the Year from the Date column
df['Year'] = df['DATE'].dt.year


# In[29]:

# Taking only the values from the datframe where year is 2016
df_1=df[df.Year==2016]
df_1


# In[30]:

# grouping all the Collisions that took place in NY during the year 2016 by month
df_NY=df_1.groupby('Month').count().reset_index()


# In[31]:

df_NY


# In[32]:

# Dropping all the unwanted columns from the dataframe
df_NY.drop(df_NY.columns[[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]], axis=1, inplace=True)


# In[33]:

df_NY.drop(df_NY.columns[[2]], axis=1, inplace=True)


# In[34]:

#renaming the columns in df_NY dataframe
df_NY.columns = ['Month','New York']


# In[35]:

# Taking only the values from the datframe df_2 where Borough is Manhattan
df_2=df_1[df_1.BOROUGH=='MANHATTAN']


# In[36]:

#Grouping the dataset df_2 by Month
df_Manhattan=df_2.groupby('Month').count().reset_index()


# In[37]:

df_Manhattan.drop(df_Manhattan.columns[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]], axis=1, inplace=True)


# In[38]:

df_Manhattan.columns = ['Month','Manhattan']


# In[39]:

# Joining the 2 datasets df_NY and df_Manhattan on Month column
result = df_NY.join(df_Manhattan.set_index('Month'), on='Month')


# In[40]:

#Calculating the Percentage of collisions that took place in Manhattan by total collision in NY during the year 2016
result['Percentage']=result['Manhattan']/result['New York']


# In[46]:

#Storing the result in csv
result.to_csv('Question1_Part1_Vehicle.csv')

