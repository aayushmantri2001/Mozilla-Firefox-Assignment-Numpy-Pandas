#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[2]:


print("Printing Original array")
Array = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (Array)


# In[4]:


sortRow = Array[Array[1,:].argsort()]
print("Sorting Original array by secoond row")
print(sortRow)


# In[5]:


sortCol= Array[Array[:,1].argsort()]
print("Sorting Original array by second column")
print(sortCol)


# In[ ]:




