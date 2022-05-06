#!/usr/bin/env python
# coding: utf-8

# # Sympy

# In[27]:


from sympy import *
import numpy as np

import sympy
#sympy.init_printing() # If all you want is the best pretty printing, use the init_printing() function.


# In[17]:


x = Symbol('x')
y = Symbol('y')


# In[18]:


(x + y)**2


# In[19]:


f = expand((x + y)**2)
display(f)


# In[20]:


f.subs({x:1, y:2})


# In[21]:


factor(x**2-4*x+3)


# In[22]:


apart(1/(x**5-1))


# In[23]:


a = Symbol('a') # Without real=True, a is treated as a complex number.
b = Symbol('b')

u = exp(a*x)*sin(b*x)
display(u)


# In[24]:


int_u = integrate(u, x)
display(int_u)


# In[25]:


R = diff(u, x, 2) + u + x
display(R)


# In[26]:


k, N = sympy.symbols('k, N', integer = True)
sympy.factor(sympy.summation(k, (k, 1, N) ))


# In[15]:


s = Symbol('s')
t = Symbol('t')

l = (s**2 * x**3) + (t * x**2) + (3 * x) + 1

int_l = integrate(l, (x, 0, 1))
display(int_l)


# In[16]:


limit(sin(x)/x, x, 0)

