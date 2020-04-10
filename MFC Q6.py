#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[ ]:


import pandas as pd


# In[ ]:


dataset = pd.read_csv("Automobile⁩_data.csv")
dataset = dataset[['company','price']][dataset.price==dataset['price'].max()]
dataset


# In[ ]:




