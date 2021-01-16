#!/usr/bin/env python
# coding: utf-8

# In[87]:


#1. Import and test 3 of the functions from your functions exercise file.

#Import each function in a different way:

#import the module and refer to the function with the . syntax

import function_exercises

function_exercises.is_two(4)


# In[2]:


#use from to import the function directly

from function_exercises import normalize_name

normalize_name('234 #$%#Hai#@%fa Isr^#ael %^##')


# In[3]:


#use from and give the function a different name

from function_exercises import handle_commas as hc

hc('1,000,000')


# In[11]:


#For the following exercises, read about and use the 
#itertools module from the standard library to help you solve the problem.


#1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?


from itertools import product

arr1 = 'abc'
arr2 = '123'

def Product(arr1,arr2):
    return list(product(arr1,arr2))
print(Product(arr1,arr2))


# In[5]:


#2. How many different ways can you combine two of the letters from "abcd"?
from itertools import combinations 
  
def rSubset(arr, r): 
  
    # return list of all subsets of length r 
    # to deal with duplicate subsets use  
    # set(list(combinations(arr, r))) 
    return list(combinations(arr, r)) 
  
# Driver Function 
if __name__ == "__main__": 
    arr = ['a','b','c','d'] 
    r = 2
    print (rSubset(arr, r)) 
 


# In[86]:


#Save this file as profiles.json inside of your exercises directory. 
#Use the load function from the json module to open this file, it will produce a list of dictionaries. 
#Using this data, write some code that calculates and outputs the following information:

import json
 

with open('profiles.json') as f:
    data = json.load(f)

    


# In[85]:


data[8]


# In[38]:


#Total number of users
#19 users
len(data)


# In[52]:


#Number of active users
#9 active
active_users = []
for user in range(len(data)):    
    if data[user]['isActive'] == True:
        active_users.append(data[user]['name'])
        
print(active_users)
len(active_users)


# In[58]:


#Number of inactive users
#10 inactive
inactive_users = []
for user in range(len(data)):    
    if data[user]['isActive'] == False:
        inactive_users.append(data[user]['name'])
        
print(inactive_users)
len(inactive_users)


# In[65]:


#Grand total of balances for all users
#52667.02
grand_total = []
for user in range(len(data)):    
    grand_total.append(data[user]['balance'])
    

def string_to_float(x):
    return float(x.replace(',','').replace('$',''))

grand_total = [string_to_float(balance) for balance in grand_total]

sum(grand_total)


# In[84]:


#Average balance per user
#2771.95
average_balance = round(sum(grand_total)/len(data),2)
average_balance


# In[83]:


#User with the lowest balance
#$1,214.10 Avery Flynn
print(min(grand_total))

[user['balance'] +' '+ user['name'] for user in data if user['balance'] == '$1,214.10']


# In[89]:


#User with the highest balance
#$3,919.64 Fay Hammond

print(max(grand_total))

[user['balance'] +' '+ user['name'] for user in data if user['balance'] == '$3,919.64']


# In[91]:


#Most common favorite fruit
#Strawberry
fav_fruit = [user['favoriteFruit'] for user in data]
fav_fruit

import statistics
statistics.mode(fav_fruit)


# In[106]:


#Least most common favorite fruit
#Apples with 4
print(sorted(fav_fruit))
print()

print('There are', fav_fruit.count('apple'), 'users with favorite Apples')
print('There are', fav_fruit.count('banana'), 'users with favorite Banana')
print('There are', fav_fruit.count('strawberry'), 'users with favorite Strawberry')


# In[115]:


#Total number of unread messages for all users
greeting = [user['greeting'] for user in data]
#print(greeting)

def extract_num(string):
    for char in string:
        if char.isdigit():
            return int(char)
        
message_quantity_list = [extract_num(message) for message in greeting]
print(f'Total number of unread messages: {sum(message_quantity_list)}')

