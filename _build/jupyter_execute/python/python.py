#!/usr/bin/env python
# coding: utf-8

# 

# # Python

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10, 100)
y = np.sin(x)

plt.plot(x,y)
plt.title('sin')
plt.show()

