#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


carsData = pd.read_csv("Macintosh HD⁩ ▸ ⁨Users⁩ ▸ ⁨aayushmantri⁩ ▸ ⁨Desktop⁩ ▸ Automobile_data.csv")
carsData = carsData.sort_values(by=['price', 'horsepower'], ascending=False)
carsData.head(5)


# In[ ]:




