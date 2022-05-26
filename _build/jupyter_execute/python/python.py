#!/usr/bin/env python
# coding: utf-8

# # Python and Jupyterlab
# 
# > Python is a clear and powerful object-oriented programming language. - python doc
# 
# > JupyterLab is a flexible, extensible interface for interactive computing. - jupyter doc
# 
# [Python](https://www.python.org/) is a simple and most popular programming language and used in many fields like AI and machine learning, Data analytics, Data visualization, Web, Game, and so on.
# 
# [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) is a next-generation web-based user interface for python programming.
# 
# Here, you can learn basics of python and usage of JupyterLab. If you have not installed jupyteer-lab, refer to [this](../basic/packageManager.md#Venv).

# ---
# ## print() function and four arithmetic operations

# In[2]:


print("Hello, world!")


# In[1]:


# This is a comment. No output.


# In[1]:


1+1


# In[4]:


print(3+4)
print('3+4')
print('3'+'4')


# In[5]:


# This will be an error. You can't add a number and a string. 
# You need to convert the string to a number or vice versa.
print(3+'4')


# In[3]:


a = 3 # This is a variable. 
b = '4'
print(a+b) # This will be the same as the above cell.


# In[4]:


print(a, b)


# In[7]:


print(a + int(b)) # This will convert the string to a number.
print(str(a) + b) # This will convert the number to a string.


# In[8]:


# Basic arithmetic operations
print('addition 1+1 = ', 1+1)
print('subtraction 5-1 = ', 5-1)
print('multiplication 2*2 = ', 2*2)
print('division 5/2 = ', 5/2)
print('modulus 5%2 = ', 5%2)
print('floor division 5//2 = ', 5//2)
print('exponentiation 5**2 = ', 5**2)


# In[9]:


# Instead of using a new line, you can use a semicolon.
print('adsf'); print('asdf')


# ---
# ## List, tuple, set, dictionary

# In[10]:


l = [3,4,5]
index = 0
print(l[index])

l[1] = 7 # You can change the value of an element in a list.
print(l)


# In[11]:


# You can use other types of data in a list.
l = [3,4,5,'a','b','c', True, False, [1,2,3]]


# In[12]:


t = (3,4,5)

# t[2] = 7
# You can't change the value of an element in a tuple.
# However, a tuple uses less memory than a list.


# In[13]:


s = {3,4,5,5}
print(s)


# In[14]:


d = {'a':3,'b':4,'c':5}
print(d['a'])

d['a'] = 6 # You can change the value of an element in a dictionary.
d['d'] = 7 # You can add a new key-value pair to a dictionary.
print(d)

print(d.items()) # This will return a list of all the key-value pairs in the dictionary.
print(d.keys()) # This will return a list of all the keys in the dictionary.
print(d.values()) # This will return a list of all the values in the dictionary.


# ---
# ## Open a file

# In[15]:


path = './sample.txt'
with open(path) as f:
    l = f.readlines()
    print(l)
    for i in range(len(l)):
        print(l[i])


# ---
# ## For loops

# In[16]:


for i in range(5):
    print(i)
# Index starts at 0.


# In[17]:


for i in range(5,10):
    print(i)
# Index starts at 5.
# cf. range(5,13,2)


# In[18]:


items = ['a','b','c','d','e']
for i in items:
    print(i)
# You can use a for loop to iterate over a list, tuple, dictionary, string, and so on.

print('-------------------------------')
for i in range(len(items)):
    print(items[i])


# In[19]:


for i, item in enumerate(items):
    print(i, item)


# In[20]:


for _ in range(5):
    print('Hello')


# ---
# ## Comprehension

# In[21]:


[i for i in range(5)]


# In[22]:


data = [3,14,23,28,35,46,55,65,76,87,98,109,120,131,142]
[x*10 for x in data]


# In[23]:


[x for x in data if x%2==0]


# In[24]:


[x if x>50 else x*10 for x in data]


# In[25]:


import numpy as np # This is a module. NumPy is a package that contains many useful functions for working with arrays.
a = np.arange(1,51)
fizz_buzz = ['fizzbuzz' if x%3==0 and x%5==0 else 'fizz' if x%3==0 else 'buzz' if x%5==0 else x for x in a]
print(fizz_buzz)


# ---
# ## Functions

# In[26]:


def print_hello():
    print('Hello, world!')


# In[27]:


print_hello()


# In[28]:


def myfunc(arg1, arg2):
    for i in range(arg1):
        print(arg2)

myfunc(3, 'Hello')
# = myfunc(arg1=3, arg2='Hello')


# In[29]:


import numpy as np
import matplotlib.pyplot as plt # Matplotlib is a package that contains many useful functions for plotting.

x = np.linspace(0,10, 100)
y = np.sin(x)

print(x[:5])
print(y[:5])


# In[30]:


plt.plot(x,y)
plt.title('sin')
plt.show()


# ### lambda functions

# $$ f(x) = x^2 $$

# In[32]:


f = lambda x: x**2

print(f(3))


# ## Reference
# [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide/Programmers)
