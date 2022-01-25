#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import random 
import math
from random import randint
import matplotlib.pyplot as plt
First = P = W = Sum = Sum1 = 0
D = 0.8
a = int(input('Введите размер матрицы: '))
J = 750 
k = [-1,1] 
mas = np.zeros((a,a))  
mas1 = 0 
debug = False
for i in range(a):
    for y in range(a):                   
        mas[i][y] = random.choice(k)         
First = mas.copy()
for Count in range(J): 
    Sum = Sum1 = 0 
    mas1 = mas.copy()
    mas1[random.randrange(a)][random.randrange(a)] *= -1    
    for k in range(a):        
        for i in range(a): 
            Sum += mas[k][i]*mas[k][i-1] + mas[k-1][i]*mas[k][i] 
            Sum1 += mas1[k][i]*mas1[k][i-1] + mas1[k-1][i]*mas1[k][i]        
    delta = (Sum1 - Sum)
    if delta <=0:
        mas = mas1.copy()
    else:
        W = math.exp(-delta/D)
        P = random.uniform(0, 1)
        if W >= P:
            First = mas.copy()
        elif W < 0:         
            mas = First.copy()
    if Count == J-1:
        if debug == True:
            for i in range(a): 
                for y in range(a):                   
                    if mas[i,y] == -1:
                        mas[i,y] = 0
        print(mas)
        print('Сумма элементов матрицы:', Sum)
plt.imshow(mas)


# In[ ]:




