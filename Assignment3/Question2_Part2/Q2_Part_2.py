
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
#reading the CSV file
df=pd.read_csv(r'employee_compensation.csv')


# In[3]:

#Filtering the dataset for only Calender year
df_Calender=df[df["Year Type"]=='Calendar']


# In[4]:

# Grouped the dataset by Job Family and employee identifier to find the mean ogf Total benefits and compensation over the years 
#for each employee
result=df_Calender.groupby(['Job Family','Employee Identifier']).mean().reset_index()


# In[5]:

#Calculating Overtime Percentage for employess over their Salaries
result['Percentage_Overtime']=(result.Overtime/result.Salaries)*100


# In[6]:

#Taking all employess whose Overtime% is greater than 5%
df_Employee=result[result.Percentage_Overtime > 5]


# In[7]:

df_Employee


# In[8]:

df_final=df_Employee.groupby('Job Family')['Total Benefits','Total Compensation'].mean().reset_index()


# In[9]:

#Calculating for each ‘Job Family’ these people are associated with,the percentage of total benefits For each ‘Job Family’ to
#total compensation 
df_final['Percentage_Total_Benefits']=(df_final['Total Benefits']*100)/df_final['Total Compensation']


# In[10]:

df_f=df_final.sort('Percentage_Total_Benefits', ascending= False , inplace=True)


# In[11]:

df_final.head()


# In[13]:

df_final.to_csv('Question2_Part2_Employee.csv')

