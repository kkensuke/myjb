#!/usr/bin/env python
# coding: utf-8

# # Sympy

# In[28]:


from sympy import *
import numpy as np

import sympy
#sympy.init_printing()


# In[29]:


x = Symbol('x')
y = Symbol('y')


# In[30]:


(x + y)**2


# In[31]:


f = expand((x + y)**2)
display(f)


# In[32]:


f.subs({x:1, y:2})


# In[33]:


factor(x**2-4*x+3)


# In[34]:


apart(1/(x**5-1))


# In[35]:


a = Symbol('a') # Without real=True, a is treated as a complex number.
b = Symbol('b')

u = exp(a*x)*sin(b*x)
display(u)


# In[36]:


int_u = integrate(u, x)
display(int_u)


# In[37]:


R = diff(u, x, 2) + u + x
display(R)


# In[38]:


k, N = sympy.symbols('k, N', integer = True)
sympy.factor(sympy.summation(k, (k, 1, N) ))


# In[39]:


s = Symbol('s')
t = Symbol('t')

l = (s**2 * x**3) + (t * x**2) + (3 * x) + 1

int_l = integrate(l, (x, 0, 1))
display(int_l)


# In[40]:


limit(sin(x)/x, x, 0)

