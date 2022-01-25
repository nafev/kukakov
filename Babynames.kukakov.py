#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import pylab 
cols = [ 'name' , 'gender', 'birth'] 
years = range(1880, 2011) 
pieces = [] 
for i in years: 
    df = pd.read_table('C:\\Users\\user\\Documents\\Python Scripts\\babynames\\yob%d.txt'%i, sep = ',', engine = 'python' , names = cols)
    df['year'] = i
    pieces.append(df)
    data = pd.concat(pieces, ignore_index = True) 
bgend=data.pivot_table('birth', index='gender', aggfunc = 'sum') 
bgend


# In[2]:


data


# In[3]:


import matplotlib.pyplot as plt 
gend=data.pivot_table('birth', index='year', columns='gender', aggfunc = 'sum')
gend
a=gend['F'] 
b=gend['M'] 
c=years 
plt.plot(c, a, label="Female", color='fuchsia', lw = 1.75) 
plt.plot(c, b, label="Male", color='steelblue', lw = 1.75)
plt.legend() 
plt.show() 


# In[4]:


nam = data.pivot_table('birth', index='year', columns='name', aggfunc='sum') 
pylab.subplot (2, 2, 1) 
pylab.plot(c, nam['Johnny'], color = 'orange') 
pylab.title('Johnny')
pylab.subplot (2, 2, 2)
pylab.plot(c, nam['Bertha'], color = 'red')
pylab.title('Bertha')
pylab.subplot (2, 2, 3)
pylab.plot(c, nam['Mattie'], color = 'green')
pylab.title('Mattie')
pylab.subplot (2, 2, 4)
pylab.plot(c, nam['Samir'], color = 'darkblue')
pylab.title('Me')


# In[5]:


a=[] 
for i in range(1880,2011):
    top= data[data['year'] == i]  
    top.sort_values('birth',ascending=False) 
    a.append(top.head(1)) 
b=pd.concat(a, ignore_index = True) 
del b['gender'] 
del b['proportion']
b


# In[ ]:




