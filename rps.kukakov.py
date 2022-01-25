#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
a = input()
choice_list = ['rock', 'paper', 'scissors']
b = random.choice(choice_list)
if (a == 'rock') and (b == 'paper'):
    print('you lose')
else:
    if (a == 'paper') and (b == 'rock'):
        print('you win')
    else:
        if (a == 'paper') and (b == 'scissors'):
            print('you lose')
        else:
            if (a == 'scissors') and (b == 'paper'):
                print('you win')
            else:
                if (a == 'scissors') and (b == 'rock'):
                    print('you lose')
                else:
                    if (a == 'rock') and (b == 'scissors'):
                        print('you win')
                    else:
                        if a == b:
                            print('draw')
print('you=',a,' computer=',b)


# In[ ]:




