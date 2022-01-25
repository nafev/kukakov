#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time 
import random
class Phone: 
    programs={} #Список для сохраниния игр 
    contaks={} #Словарь для контактов
    def __init__(self,the_brand, model, CPU ,RAM, battery, display,storage):
        self.name = the_brand   #сохраняем переменные для данного класса
        self.model = model
        self.the_brand = CPU
        self.cooler = RAM
        self.power_unit = battery
        self.GPU = display
        self.storage=storage 
        #ниже вспомогательные переменные данного гласса
        self.storage_status = 0 #storage показывает максимальное кол-во места,storage_status показывает текущее заполнение 
        print(f'Вы купили новый телефон:{self.name}') 
   

    def contaks_adds(self):
        number =int(input('Введите номер: '))
        name = (input('Введите Имя: '))
        Phone.contaks[name] = number
        self.storage_status += 0.00003
        print(f'Котнакт {name} добавлен' )
    
    def contaks_del(self):
        print(Phone.contaks.keys())
        name = input('какой контакт хотите удалить: ')
        del Phone.contaks[name]
        self.storage_status -= 0.00003
        print(f'Контакт {name} удален' )
    
    def call_contakt(self):
        print(Phone.contaks.keys())
        name = input('Кому звоним: ')
        print('вы позвонили', name )
    
    def Programs(self):
        if  self.storage_status < self.storage:
            program =input('Название программы: ')
            size = random.randint(2,60)
            Phone.programs[program] = size
            self.storage_status +=size
            print(f'Программа {program} установлена' )
        else:print('Диск переполнен')
            
    def Programs_del(self,):
        print(Phone.programs.keys())
        program = input('Введите програму которую хотите удалить: ')
        size=Phone.programs[program]
        del Phone.programs[program]
        self.storage_status -=size
        print(f'Вы удалили: {program}')
        
    def paly(self):
        print(Phone.programs.keys())
        program = input('Введите програму которую хотите запустить: ')
        print(program, 'Запущена')


# In[3]:


My_Phone = Phone ( 'Samsung', " A71" , "Snapdragon 810", "8gb",'5000mh', 'OLED',512)


# In[4]:


My_Phone.contaks_adds()


# In[7]:


My_Phone.contaks_del()


# In[8]:


My_Phone.Programs()


# In[9]:


My_Phone.Programs_del()


# In[13]:


My_Phone.call_contakt()


# In[10]:


My_Phone.paly()


# In[ ]:




