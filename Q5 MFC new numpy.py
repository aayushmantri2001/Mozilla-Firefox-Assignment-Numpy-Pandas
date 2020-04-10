#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy


# In[5]:


arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])


# In[6]:


Array  = arrayOne + arrayTwo
print("addition of two arrays is ")
print(Array)


# In[13]:


for num in numpy.nditer(Array,op_flags = ['readwrite']):
   num[...] = num*num
print("Result array after calculating the square root of all elements")
print(Array)


# In[ ]:




