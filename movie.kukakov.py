#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
vnames = ['UserID', 'gender', 'age', 'occupation', 'Zip-code']
users = pd.read_table('C:\\Users\\user\\Documents\\Python Scripts\\movielens\\users.dat', sep='::', engine='python', names=vnames)
rate=['UserID','MovieID','Rating','Timestamp']
ratings=pd.read_table('C:\\Users\\user\\Documents\\Python Scripts\\movielens\\ratings.dat',sep='::', engine='python', names=rate)
usrate = pd.merge(ratings, users)
usrate


# In[5]:


import pandas as pd
films=['MovieID', 'Title', 'Jenre']
movies=pd.read_table('C:\\Users\\user\\Documents\\Python Scripts\\movielens\\movies.dat', sep='::', engine='python', names=films, encoding='latin-1')
usramo = pd.merge(usrate, movies)
usramo


# In[6]:


srate = usramo.pivot_table('Rating', index='Title', columns='gender', aggfunc = 'mean')
srate


# In[7]:


sage = usramo.pivot_table('Rating', index='Title', columns='age', aggfunc = 'mean')
sage


# In[8]:


resultg = srate.sort_values('F', axis=0, ascending=False)
resultg


# In[9]:


resulta = sage.sort_values(56, axis=0, ascending=True)
resulta


# In[10]:


r_b_title = usramo.groupby('Title')
l = r_b_title.size ()
resultR = l.sort_values()
resultR[resultR >= 250]


# In[11]:


srate = usramo.pivot_table('Rating', index='Title', columns='gender', aggfunc = 'mean')
DIF=srate['F'] - srate['M']
resultDIF = DIF
DIF[DIF >= 0]


# In[12]:


srate = usramo.pivot_table('Rating', index='Title', columns='gender', aggfunc = 'mean')
DIF=srate['F'] - srate['M'] 
resultDIF = DIF.sort_values(ascending=False)
k = resultDIF[resultDIF >=0]
m = k.head(15)
m


# In[13]:


rate = usramo.pivot_table('Rating', index='Title', columns='gender', aggfunc = 'mean')
DIF=srate['M'] - srate['F'] 
resultDIF = DIF.sort_values(ascending=False)
k = resultDIF[resultDIF >= 0]
m = k.head(15)
m


# In[ ]:




