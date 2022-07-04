#!/usr/bin/env python
# coding: utf-8

# # [SymPY](https://www.tutorialspoint.com/sympy/index.htm)
# > SymPy is a Python library for symbolic mathematics. - sympy doc
# 
# In this page, you see examples of sympy usage.

# In[4]:


from sympy import *


# ## Declare symbols

# In[5]:


x = Symbol('x')
y = Symbol('y')


# In[6]:


(x + y)**2


# ## Expansion

# In[7]:


f = expand((x + y)**2)
display(f)


# ## Substitution

# In[8]:


f.subs({x:1, y:2})


# ## Factorization

# In[9]:


factor(x**2-4*x+3)


# ## Solve equations

# In[10]:


solve(x**2 - x - 1)


# ## Partial fraction decomposition

# In[11]:


apart(1/(x**5-1))


# ## Integrals and derivatives

# In[12]:


a = Symbol('a') # Without real=True, a is treated as a complex number.
b = Symbol('b')

u = exp(a*x)*sin(b*x)
display(u)


# In[13]:


int_u = integrate(u, x)
display(int_u)


# In[14]:


R = diff(u, x, 2) + u + x
display(R)


# ## Summation

# In[15]:


k, N = symbols('k, N', integer = True)
factor(summation(k, (k, 1, N) ))


# ## Limits

# In[18]:


limit(sin(x)/x, x, 0)


# ## Other Examples

# In[16]:


s = Symbol('s')
t = Symbol('t')

l = (s**2 * x**3) + (t * x**2) + (3 * x) + 1

display(l)


# In[17]:


int_l = integrate(l, (x, 0, 1))
display(int_l)

