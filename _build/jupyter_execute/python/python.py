#!/usr/bin/env python
# coding: utf-8

# 

# # Python and Jupyter

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


# In[27]:


# This will be an error. You can't add a number and a string. 
# You need to convert the string to a number or vice versa.
# print(3+'4')


# In[28]:


a = 3 # This is a variable. 
b = '4'
# print(a+b) # This will be the same as the above cell.


# In[29]:


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


# Instead of using a new line, you can use a semicolon.
print('adsf'); print('asdf')


# ## List, tuple, set, dictionary

# In[17]:


l = [3,4,5]
index = 0
print(l[index])

l[1] = 7 # You can change the value of an element in a list.
print(l)


# In[31]:


# You can use other types of data in a list.
l = [3,4,5,'a','b','c', True, False, [1,2,3]]


# In[30]:


t = (3,4,5)

# t[2] = 7
# You can't change the value of an element in a tuple.
# However, a tuple uses less memory than a list.


# In[22]:


s = {3,4,5,5}
print(s)


# In[34]:


d = {'a':3,'b':4,'c':5}
print(d['a'])

d['a'] = 6 # You can change the value of an element in a dictionary.
d['d'] = 7 # You can add a new key-value pair to a dictionary.
print(d)

print(d.items()) # This will return a list of all the key-value pairs in the dictionary.
print(d.keys()) # This will return a list of all the keys in the dictionary.
print(d.values()) # This will return a list of all the values in the dictionary.


# ## Open a file

# In[ ]:


path = './sample.txt'
with open(path) as f:
    l = f.readlines()
    print(l)
    for i in range(len(l)):
        print(l[i])


# ## For loops

# In[2]:


for i in range(5):
    print(i)
# Index starts at 0.


# In[3]:


for i in range(5,10):
    print(i)
# Index starts at 5.
# cf. range(5,13,2)


# In[6]:


items = ['a','b','c','d','e']
for i in items:
    print(i)
# You can use a for loop to iterate over a list, tuple, dictionary, string, and so on.

print('-------------------------------')
for i in range(len(items)):
    print(items[i])


# In[7]:


for i, item in enumerate(items):
    print(i, item)


# In[8]:


for _ in range(5):
    print('Hello')


# ## Comprehension

# In[9]:


[i for i in range(5)]


# In[14]:


data = [3,14,23,28,35,46,55,65,76,87,98,109,120,131,142]
[x*10 for x in data]


# In[12]:


[x for x in data if x%2==0]


# In[15]:


[x if x>50 else x*10 for x in data]


# In[16]:


import numpy as np # This is a module. NumPy is a package that contains many useful functions for working with arrays.
a = np.arange(1,51)
fizz_buzz = ['fizzbuzz' if x%3==0 and x%5==0 else 'fizz' if x%3==0 else 'buzz' if x%5==0 else x for x in a]
print(fizz_buzz)


# ## Functions

# In[25]:


def print_hello():
    print('Hello, world!')


# In[26]:


print_hello()


# In[17]:


def myfunc(arg1, arg2):
    for i in range(arg1):
        print(arg2)

myfunc(3, 'Hello')
# = myfunc(arg1=3, arg2='Hello')


# In[2]:


import numpy as np
import matplotlib.pyplot as plt # Matplotlib is a package that contains many useful functions for plotting.

x = np.linspace(0,10, 100)
y = np.sin(x)

print(x)
print(y)


# In[3]:


plt.plot(x,y)
plt.title('sin')
plt.show()


# ## lambda functions

# $$ f(x) = x^2 $$

# In[4]:


f = lambda x: x**2
print(f(3))


# $$ f(x, t; a, b, v) = \frac{1}{\pi} \frac{2tbv}{(vt)^2 + (x-a)^2} $$
# $$ a,b,v \,\text{are parameters}$$

# In[5]:


a = 1
b = 0.01
v = 1

func = lambda x, t: b*v**2*t/(v**2*t**2 + (x-a)**2)/np.pi

x = np.linspace(-10,10,1000)
t  =np.array([1,2,3,4,5])
for it in t: 
    y = func(x, np.ones(1000)*it)
    plt.plot(x,y, label = 't = {}'.format(it))
    plt.legend()

