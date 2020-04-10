#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[2]:


Array = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]]) 
print("Printing Input Array")
print(Array)


# In[5]:


print("Printing array of items in the third column from all rows")
NArray =Array[...,2]
print(NArray)


# In[ ]:




