#!/usr/bin/env python
# coding: utf-8

# 

# # Python

# ## four arithmetic operations and print() function

# In[2]:


1+1


# In[3]:


print("Hello, world!")


# In[14]:


# This is a comment. It is not executed.


# In[8]:


print(3+4)
print('3+4')
print('3'+'4')


# In[7]:


print(3+'4') # This will be an error. You can't add a number and a string. You need to convert the string to a number or vice versa.


# In[9]:


a = 3 # This is a variable. 
b = '4'
print(a+b) # This will be the same as the above cell.


# In[10]:


print(a + int(b)) # This will convert the string to a number.
print(str(a) + b) # This will convert the number to a string.


# In[1]:


# Basic arithmetic operations
print('addition 1+1 = ',1+1)
print('subtraction 5-1 = ',5-1)
print('multiplication 2*2 = ',2*2)
print('division 5/2 = ',5/2)
print('modulus 5%2 = ',5%2)
print('floor division 5//2 = ',5//2)
print('exponentiation 5**2 = ',5**2)


# In[12]:


print('adsf'); print('asdf') # Instead of using a new line, you can use a semicolon.


# ## List, tuple, set, dictionary

# In[17]:


l = [3,4,5]
index = 0
print(l[index])

l[1] = 7 # You can change the value of an element in a list.
print(l)


# In[19]:


t = (3,4,5)

t[2] = 7 # You can't change the value of an element in a tuple.


# In[22]:


s = {3,4,5,5}
print(s)


# In[24]:


d = {'a':3,'b':4,'c':5}
print(d['a'])

d['a'] = 6 # You can change the value of an element in a dictionary.
d['d'] = 7 # You can add a new key-value pair to a dictionary.
print(d)


# ## Functions

# In[25]:


def print_hello():
    print('Hello, world!')


# In[26]:


print_hello()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10, 100)
y = np.sin(x)

plt.plot(x,y)
plt.title('sin')
plt.show()

