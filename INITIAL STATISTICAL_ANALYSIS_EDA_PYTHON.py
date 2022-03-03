#!/usr/bin/env python
# coding: utf-8

# In[10]:


#STATISTICAL ANALYSIS USING PYTHON
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.gridspec import GridSpec
pd.set_option('display.max_columns', 100)
import plotly.offline as py
import plotly.express as px
import plotly.graph_objs as go
import json
import requests


# In[11]:


Data = pd.read_csv("O-LIST_after_Merge.csv")
print(Data)


# In[12]:


Data.head()


# In[13]:


Data.info()


# In[14]:


Data.describe()


# In[19]:


#Correlation matrix 
correlation_matrix = Data.corr()


# In[21]:


plt.figure(figsize=(18,8))
sns.set(font_scale=1.3)
cmap = sns.light_palette("#800080",as_cmap=True)
sns.heatmap(correlation_matrix, cmap=cmap,annot=True)
plt.title("  Correlation Matrix",fontsize=19)
plt.savefig('plot16.png', dpi=300, bbox_inches='tight')
plt.show()


# In[ ]:


#WE FIND A HIGHER DEGREE OF CORRELATION AMONG THE FOLLOWING ATTRIBUTES:
payment and price, product lenght & width, height & weight, weight & frieght value


# In[22]:


# WE FIND THE MOST FREQUENTLY USED PAYMENT METHOD: 

Data.payment_type.mode()


# In[23]:


print(Data.payment_type)


# In[24]:


Data.payment_type.value_counts()


# In[ ]:


# AS WE SEE CREDIT CARD, BOLETO, VOUCHER ARE THE MAXIMUM USED MODE OF PAYMENT


# In[25]:


Data.review_score.mean()


# In[ ]:


#WE SEE THAT THE MEAN REVIEW SCORE IS 4.09 WHICH IS GOOD 


# In[26]:


Data.review_score.median()


# In[27]:


Data.review_score.mode()


# In[28]:


Data.review_score.value_counts()


# In[ ]:


#we see that maximum review score is either 5 or 4 followed by 1 

