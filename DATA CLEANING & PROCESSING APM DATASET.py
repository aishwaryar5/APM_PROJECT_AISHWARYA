#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#DATA CLEANING AND PROCESSING


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import statistics
import time


# In[3]:


data1 = pd.read_csv("olist_customers_dataset.csv")
data2 = pd.read_csv("olist_geolocation_dataset.csv")
data3  = pd.read_csv("olist_order_items_dataset.csv")
data4 = pd.read_csv("olist_order_payments_dataset.csv")
data5 = pd.read_csv("olist_order_reviews_dataset.csv")
data6  = pd.read_csv("olist_orders_dataset.csv")
data7  = pd.read_csv("olist_products_dataset.csv")
data8  = pd.read_csv("olist_sellers_dataset.csv")


# In[4]:



#NULL HANDLING & HANDLING MISSING VALUE

data_sets = [data1,data2,data3,data4,data5,data6,data7,data8]
ColumnNames_ = ["customers","locations","items", "payments", "orders", "products","reviews","sellers"]

Data_handling = pd.DataFrame({},)

Data_handling['data_sets']= ColumnNames_ 
Data_handling['columns'] = [', '.join([col for col, null in df.isnull().sum().items() ]) for df in data_sets]



#NULL VALUES COUNT:
Data_handling['null count']= [df.isnull().sum().sum() for df in data_sets] 
Data_handling['null column count']= [len([col for col, null in df.isnull().sum().items() if null > 0]) for df in data_sets]

Data_handling['null columns'] = [', '.join([col for col, null in df.isnull().sum().items() if null > 0]) for df in data_sets]

print(Data_handling)


# In[5]:


Data_handling.style.background_gradient(cmap='coolwarm')


# In[6]:


#INSIGHTS:
#    WE SEE THAT THE ORDERS DATASET AND PRODUCTS DATASET HAVE THE HIGHEST NUMBER OF NULLVALUES. 
#     THE REVIEW DATA SET HAS LESS NUMBER OF NULLS BUT IT HAS NULL VALUES IN ALL 8 COLUMNS, THE SELLER,
#     PAYMENTS,ITEMS,LOCATIONS & CUSTOMERS DO NOT HAVE ANY NULL VALUES.
   


# In[7]:


# MERGING DATA AND NULL HANDLING 


# In[8]:


customer = pd.read_csv("olist_customers_dataset.csv")
geolocation = pd.read_csv("olist_geolocation_dataset.csv")
item  = pd.read_csv("olist_order_items_dataset.csv")
payment = pd.read_csv("olist_order_payments_dataset.csv")
review = pd.read_csv("olist_order_reviews_dataset.csv")
order  = pd.read_csv("olist_orders_dataset.csv")
product  = pd.read_csv("olist_products_dataset.csv")
seller  = pd.read_csv("olist_sellers_dataset.csv")


# In[12]:



df = pd.merge(order,payment, on="order_id")
df = df.merge(customer, on="customer_id")
df = df.merge(item, on="order_id")
df = df.merge(product, on="product_id")
df = df.merge(seller, on="seller_id")
df = df.merge(review, on="order_id")
df.head()


# In[13]:


print(df)


# In[20]:


print("rows after merge:",len(df))
print("columns after merge:",len(df.columns))


# In[16]:


df.isnull().sum()


# In[19]:


#HANDLING NULL VALUES 
index = (df[df['order_delivered_customer_date'].isnull() == True].index.values)

df["order_approved_at"].fillna(df["order_purchase_timestamp"], inplace=True)
df["order_delivered_customer_date"].fillna(df["order_estimated_delivery_date"], inplace=True)
df['product_weight_g'].fillna(df['product_weight_g'].median(),inplace=True)
df['product_length_cm'].fillna(df['product_length_cm'].median(),inplace=True)
df['product_height_cm'].fillna(df['product_height_cm'].median(),inplace=True)
df['product_width_cm'].fillna(df['product_width_cm'].median(),inplace=True)
#dropping order delivery carrier date
#df.drop(labels='order_delivered_carrier_date',axis=1,inplace=True)


# In[21]:


#IDENTIFYING DUPLICATE VALUES
duplicateValues = df[df.duplicated(['order_id','customer_id','order_purchase_timestamp','order_delivered_customer_date','customer_unique_id','review_comment_message'])]
duplicateValues.head()


# In[22]:


print(duplicateValues)


# In[23]:


#REMOVING DUPLICATE ENTRIES OR DE-DUPLICATION
df= df.drop_duplicates(subset={'order_id','customer_id','order_purchase_timestamp','order_delivered_customer_date'}, keep='first', inplace=False)
df=df.reindex()
df.head()


# In[24]:


#ROWS AND COLUNS AFTER DE-DUPLICATION
print("Number of rows:",len(df))
print("Number of columns:",len(df.columns))


# In[ ]:




