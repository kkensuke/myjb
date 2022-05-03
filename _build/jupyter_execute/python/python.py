#!/usr/bin/env python
# coding: utf-8

# 

# # Python

# ## Basic arithmetic operations

# In[2]:


1+1


# In[3]:


print("Hello, world!")


# In[1]:


print('addition 1+1 = ',1+1)
print('subtraction 5-1 = ',5-1)
print('multiplication 2*2 = ',2*2)
print('division 5/2 = ',5/2)
print('modulus 5%2 = ',5%2)
print('floor division 5//2 = ',5//2)
print('exponentiation 5**2 = ',5**2)


# In[ ]:





# In[2]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10, 100)
y = np.sin(x)

plt.plot(x,y)
plt.title('sin')
plt.show()

