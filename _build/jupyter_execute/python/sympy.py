#!/usr/bin/env python
# coding: utf-8

# # [SymPY](https://www.tutorialspoint.com/sympy/index.htm)
# > SymPy is a Python library for symbolic mathematics. - sympy doc
# 
# In this page, you see examples of sympy usage.

# In[1]:


from sympy import *


# In[2]:


x = Symbol('x')
y = Symbol('y')


# In[3]:


(x + y)**2


# In[4]:


f = expand((x + y)**2)
display(f)


# In[5]:


f.subs({x:1, y:2})


# In[6]:


factor(x**2-4*x+3)


# In[7]:


solve(x**2 - x - 1)


# In[8]:


apart(1/(x**5-1))


# In[9]:


a = Symbol('a') # Without real=True, a is treated as a complex number.
b = Symbol('b')

u = exp(a*x)*sin(b*x)
display(u)


# In[10]:


int_u = integrate(u, x)
display(int_u)


# In[11]:


R = diff(u, x, 2) + u + x
display(R)


# In[12]:


k, N = symbols('k, N', integer = True)
factor(summation(k, (k, 1, N) ))


# In[ ]:


s = Symbol('s')
t = Symbol('t')

l = (s**2 * x**3) + (t * x**2) + (3 * x) + 1

int_l = integrate(l, (x, 0, 1))
display(int_l)


# In[ ]:


limit(sin(x)/x, x, 0)

