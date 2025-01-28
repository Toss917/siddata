#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd


# In[7]:


df = pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\attrition.csv")


# In[8]:


df.head()


# In[9]:


df.columns


# In[10]:


df.shape  # check for row and colum


# In[11]:


import seaborn as sns # update varsion of matplotlib
import matplotlib.pyplot as plt # using for drawing is an open-source drawing library 
import plotly.io as pio   # using for templates 
import plotly.graph_objects as go
pio.templates.deafult = "plotly.white"   # using for fix tamplates colour 


# In[12]:


df.isnull().sum()  #this is use for cjeck missing value 


# # Filter the to show only " yes " value in the "attriation" column
# 

# In[13]:


att_df = df[df['Attrition'] == 'Yes']  


# In[14]:


att_df


# # Calculate the attrition by DEpartment 
# 

# In[15]:


attrition_by_dept = att_df.groupby(['Department']).size().reset_index(name = "count")
attrition_by_dept


# In[23]:


fig = go.Figure(data = [go.Pie(
      labels = attrition_by_dept['Department'],
      values= attrition_by_dept['count'],
      hole = 0.4,
      marker = dict(colors = ['green','yellow']),
      textposition = 'inside'
)])

fig.update_layout(title = 'attrition by Department')
fig.show()


# # Calculate the attrition by education field

# In[25]:


attrition_by_edu = att_df.groupby(['EducationField']).size().reset_index(name = "count")
attrition_by_edu


# In[26]:


fig = go.Figure(data = [go.Pie(
      labels = attrition_by_edu['EducationField'],
      values= attrition_by_edu['count'],
      hole = 0.4,
      marker = dict(colors = ['green','yellow']),
      textposition = 'inside'
)])

fig.update_layout(title = 'attrition by Education Field')
fig.show()


# # Now lets have a look at the percentage of attrition by number of years at the company

# In[28]:


attrition_by = att_df.groupby(['YearsAtCompany']).size().reset_index(name = "count")
attrition_by


# In[29]:


fig = go.Figure(data = [go.Pie(
      labels = attrition_by['YearsAtCompany'],
      values= attrition_by['count'],
      hole = 0.4,
      marker = dict(colors = ['green','yellow']),
      textposition = 'inside'
)])

fig.update_layout(title = 'attrition by YearsAtCompany')
fig.show()


# In[ ]:




