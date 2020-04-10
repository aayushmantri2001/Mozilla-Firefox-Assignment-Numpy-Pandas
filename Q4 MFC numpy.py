#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[2]:


Array = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]]) 
print("Printing Input Array")
print(Array)


# In[3]:


print("\n Printing array of odd rows and even columns")
NArray = Array[::2, 1::2]
print(NArray)


# In[ ]:




