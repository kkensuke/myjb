#!/usr/bin/env python
# coding: utf-8

# # Sympy

# In[8]:


from sympy import *
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import display

import sympy
sympy.init_printing() # If all you want is the best pretty printing, use the init_printing() function.


# In[9]:


x = Symbol('x')
y = Symbol('y')


# In[10]:


(x + y)**2


# In[11]:


f = expand((x + y)**2)
display(f)


# In[12]:


f.subs({x:1, y:2})


# In[13]:


factor(x**2-4*x+3)


# In[14]:


apart(1/(x**5-1))


# In[15]:


a = Symbol('a') # Without real=True, a is treated as a complex number.
b = Symbol('b')

u = exp(a*x)*sin(b*x)
display(u)


# In[16]:


int_u = integrate(u, x)
display(int_u)


# In[17]:


R = diff(u, x, 2) + u + x
display(R)


# In[18]:


k, N = sympy.symbols('k, N', integer = True)
sympy.factor(sympy.summation(k, (k, 1, N) ))


# In[19]:


s = Symbol('s')
t = Symbol('t')

l = (s**2 * x**3) + (t * x**2) + (3 * x) + 1

int_l = integrate(l, (x, 0, 1))
display(int_l)


# In[16]:


limit(sin(x)/x, x, 0)

