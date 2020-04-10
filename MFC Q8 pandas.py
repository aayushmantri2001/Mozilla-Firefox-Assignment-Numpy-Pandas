#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)


# In[3]:


japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)


# In[6]:


carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
carsDf


# In[ ]:




