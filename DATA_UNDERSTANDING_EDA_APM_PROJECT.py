#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import matplotlib.pyplot as plt
import statistics
import time


# In[7]:


data = pd.read_csv('olist_customers_dataset.csv')
data.head()
print(data)


# In[8]:


data1 = pd.read_csv('olist_order_items_dataset.csv')
data1.head()


# In[9]:


print(data1)


# In[11]:


data2 = pd.read_csv('olist_order_payments_dataset.csv')
data2.head()


# In[12]:


print(data2)


# In[13]:


data3 = pd.read_csv('olist_order_reviews_dataset.csv')
data3.head()


# In[14]:


print(data3)


# In[17]:


data4 = pd.read_csv('olist_orders_dataset.csv')
data4.head()


# In[18]:


print(data4)


# In[19]:


data5 = pd.read_csv('olist_products_dataset.csv')
data5.head()


# In[20]:


print(data5)


# In[21]:


data6 = pd.read_csv('olist_sellers_dataset.csv')
data6.head()


# In[22]:


print(data6)


# In[25]:


timebegin = time.time()
data1 = pd.read_csv("olist_customers_dataset.csv")
data2 = pd.read_csv("olist_geolocation_dataset.csv")
data3  = pd.read_csv("olist_order_items_dataset.csv")
data4 = pd.read_csv("olist_order_payments_dataset.csv")
data5 = pd.read_csv("olist_order_reviews_dataset.csv")
data6  = pd.read_csv("olist_orders_dataset.csv")
data7  = pd.read_csv("olist_products_dataset.csv")
data8  = pd.read_csv("olist_sellers_dataset.csv")
timeend = time.time()
print("total reading  time: ",(timeend-timebegin),"sec")


# In[33]:


# DATA TYPE IDENTIFICATION
data_types = [data1,data2,data3,data4,data5,data6,data7,data8]
titles = ["customers","locations","items", "payments", "orders", "products","reviews","sellers"]
values = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64','Char']
df_for_dtype = pd.DataFrame({},)
df_for_dtype['data_types']= titles


# In[39]:



df_for_dtype['Integer_features'] = [len((df.select_dtypes(include='int')).columns) for df in data_types]
df_for_dtype['numeric_features'] = [len((df.select_dtypes(include=values)).columns) for df in data_types]
df_for_dtype['num_features_name'] = [', '.join(list((df.select_dtypes(include=values)).columns)) for df in data_types]
df_for_dtype['object_features'] = [len((df.select_dtypes(include='object')).columns) for df in data_types]
df_for_dtype['object_features_name'] = [', '.join(list((df.select_dtypes(include='object')).columns)) for df in data_types]
df_for_dtype['boolean_features'] = [len((df.select_dtypes(include='bool')).columns) for df in data_types]


# In[40]:


print(df_for_dtype)


# In[ ]:


# WE IDENTIFIED THAT OUR DATA SET HAS A TOTAL OF : 
    # 19 NUMERIC DATA ATTRIBUTES  & 31 STRING (OR) CHARACTER ATTRIBUTES

