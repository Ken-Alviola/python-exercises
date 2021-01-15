#!/usr/bin/env python
# coding: utf-8

# Exercises
# 
# Create a file named function_exercises.py for this exercise.
# After creating each function specified below, write the necessary code in order to test your function.

# In[6]:


#1. Define a function named is_two. It should accept one input and return True
# if the passed input is either the number or the string 2, False otherwise.

def is_two(num):
    return num == 2 or num == '2'

is_two(4)


# In[7]:


#2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

vowels = ['a','e','i','o','u']

def is_vowel(value):
   
    answer = False

    if value.lower() in vowels:
        answer = True
    else:
        answer = False
    return answer

is_vowel('a')


# In[137]:


#3. Define a function named is_consonant. It should return True if the passed string is a consonant,
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(value):
   
    return not is_vowel(value)

is_consonant('p')


# In[18]:


#4. Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of the word if the word starts with a consonant.


def cap_consonant(word):
    if word[0] not in vowels:
        word = word.capitalize()
    return word

cap_consonant('rum')


# In[24]:


#5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(total,percentage):
    return f'${total * percentage}'

calculate_tip(15.00,0.2)


# In[26]:


#6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(price,discount):
    price_with_discount = price - (price * discount)
    return price_with_discount

apply_discount(20.0,0.1)


# In[30]:


#7. Define a function named handle_commas. It should accept a string that is a number that contains commas
# in it as input, and return a number as output.

def handle_commas(x):
    return int(x.replace(',',''))

handle_commas('1,000,000')


# In[41]:


#8. Define a function named get_letter_grade. It should accept a number and return the letter grade
# associated with that number (A-F).

def get_letter_grade(number_grade):
    if number_grade in range(90,101):
        return 'A'
    elif number_grade in range(80,90):
        return 'B'
    elif number_grade in range(70,80):
        return 'C'
    elif number_grade in range(60,70):
        return 'D'
    else:
        return 'F'
    
get_letter_grade(88)


# In[57]:


#9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    word = word.lower()
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, '')
    return word

remove_vowels('AdbEiyTo')


# In[122]:


'''
10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
anything that is not a valid python identifier should be removed
leading and trailing whitespace should be removed
everything should be lowercase
spaces should be replaced with underscores
for example:
Name will become name
First Name will become first_name
% Completed will become completed
'''

def normalize_name(name):
    
    # print('#1. new list: \n',name)
    name = [char for char in name if char.isalnum() or char == ' ']
     # print('#2. join char:  \n',name)
    name = ''.join([str(char) for char in name])
   
    return name.strip().lower().replace(' ','_')

normalize_name('  % RATATA@$#&^TATA Pac(^#$ifica $@#$lolwut! ')


# In[81]:


'''
11. Write a function named cumulative_sum that accepts a list of numbers and returns a 
list that is the cumulative sum of the numbers in the list.
cumulative_sum([1, 1, 1]) returns [1, 2, 3]
cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
Additional Exercise
'''

def cumulative_sum(numlist):
    cu_list = [] 
    length = len(numlist) 
    cu_list = [sum(numlist[0:x:1]) for x in range(0, length+1)] 
    return cu_list[1:]

cumulative_sum([1,2,3,4])
    


# In[136]:


#Once you've completed the above exercises, follow the directions from 
#https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

#Bonus

#1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and 
# return a string that is the representation of the time in a 24-hour format. 

def twelveto24(str1):
    
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:5] 
  
        
print(twelveto24("10:05PM")) 


#Bonus write a function that does the opposite.


# In[130]:


#2. Create a function named col_index. It should accept a spreadsheet column name,
# and return the index number of the column.
# - col_index('A') returns 1
# - col_index('B') returns 2
# - col_index('AA') returns 27




# In[ ]:




