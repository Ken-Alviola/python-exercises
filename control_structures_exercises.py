#!/usr/bin/env python
# coding: utf-8

# # Exercises
# 
# # Do your work for this exercise in a file named control_structures_exercises.py.
# 
# # 1 Conditional Basics
# 

# In[158]:


# a. prompt the user for a day of the week, print out whether the day is Monday or not

today = input('What day is it today? ')

if today == 'Monday':
    print('Today is Monday my dudes.')
else:
    print('Today is not Monday my dudes.')


# In[160]:


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

weekend = ['Saturday','Sunday']
day_of_week = input('What day is it my dude?: ')
day_of_week = day_of_week.capitalize()

if day_of_week in weekend:
    print("It's the weekend my dude.")
else:
    print("It's a weekday my dude.")


# In[161]:


# c. create variables and make up values for

hours_worked = 60 # -the number of hours worked in one week
hourly_rate = 40 # -the hourly rate
this_weeks_pay = hourly_rate * hours_worked # -how much the week's paycheck will be
# -write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours
if hours_worked <= 40:
    this_weeks_pay = hourly_rate * hours_worked
else:
    this_weeks_pay = (hourly_rate * 40) + (1.5*hourly_rate)*(hours_worked - 40)
    
this_weeks_pay


# In[162]:


# 2. Loop Basics

#a. While

# -Create an integer variable i with a value of 5.
# -Create a while loop that runs so long as i is less than or equal to 15
# -Each loop iteration, output the current value of i, then increment i by one.
# -Your output should look like this:

'''
5
6
7
8
9
10
11
12
13
14
15
'''
i = 5 
while i <= 15:
    print('i = ',i)
    i += 1
    


# In[163]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
n = 0
while n <= 100:
    print(n)
    n += 2


# In[164]:


# Alter your loop to count backwards by 5's from 100 to -10.
n = 100
while n >= -10:
    print(n)
    n -= 5


# In[165]:


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

'''
 2
 4
 16
 256
 65536
 '''

n = 2
while n <= 1_000_000:
    print (n)
    n = n ** 2
    


# In[166]:


# -Write a loop that uses print to create the output shown below.

'''
100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
'''
n = 100
while n >= 5:
    print(n)
    n -= 5


# In[167]:


# b. For Loops

# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# For example, if the user enters 7, your program should output:

'''
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
'''
num = int(input('Enter an integer my dude: '))

count = 1
for number in range(10):
    print (f'{num} x {count} = {num * count}')
    count += 1


# In[168]:


# ii. Create a for loop that uses print to create the output shown below.

'''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
n = 1
count = 1
for number in range(9):
    print (f'{str(n) * count}')
    n += 1
    count += 1
           


# In[170]:


# c. break and continue

# i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to 
# continue prompting the user if they enter invalid input.
# (Hint: use the isdigit method on strings to determine this). 

odd_num = ''

while not odd_num.isdigit() or (int(odd_num) % 2 == 0) or int(odd_num) < 1 or int(odd_num) > 50:
    odd_num = input('Enter an odd number between 1 and 50: ')
    if odd_num.isdigit() and (int(odd_num) % 2 != 0) and int(odd_num) >= 1 and int(odd_num) < 50:
        break
    
print('Thanks for following directions') 
        
    


# In[171]:


# Use a loop and the continue statement to output all the odd numbers between 1 and 50,
# except for the number the user entered.

# Your output should look like this:

'''
Number to skip is: 27

Here is an odd number: 1
Here is an odd number: 3
Here is an odd number: 5
Here is an odd number: 7
Here is an odd number: 9
Here is an odd number: 11
Here is an odd number: 13
Here is an odd number: 15
Here is an odd number: 17
Here is an odd number: 19
Here is an odd number: 21
Here is an odd number: 23
Here is an odd number: 25
Yikes! Skipping number: 27
Here is an odd number: 29
Here is an odd number: 31
Here is an odd number: 33
Here is an odd number: 35
Here is an odd number: 37
Here is an odd number: 39
Here is an odd number: 41
Here is an odd number: 43
Here is an odd number: 45
Here is an odd number: 47
Here is an odd number: 49
'''
n = 0
skip = int(input('Enter an odd number between 1 and 50 to skip: '))
print(f'Number to skip is: {skip}\n')

for n in range (50):
    if n % 2 == 0:
        continue
    elif n == skip:
        print(f'Yikes! Skipping number: {skip}')
    else:
        print(f'Here is an odd number: {n}')


# In[172]:


# d. The input function can be used to prompt for input and use that input in your python code.
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#(Hints: first make sure that the value the user entered is a valid number,
#also note that the input function returns a string, so you'll need to convert this to a numeric type.)

num = int(input('Enter a + integer: '))
count = 0

for n in range(0,num + 1):
    print(count)
    count += 1
    


# In[173]:


# e. Write a program that prompts the user for a positive integer.
#Next write a loop that prints out the numbers from the number the user entered down to 1.

num = int(input('Enter a + integer: '))

for n in range(num,0,-1):
    print(num)
    num -= 1


# In[174]:


# 3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
#Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# -Write a program that prints the numbers from 1 to 100.
# -For multiples of three print "Fizz" instead of the number
# -For the multiples of five print "Buzz".
# -For numbers which are multiples of both three and five print "FizzBuzz".


for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print ('FizzBuzz')
    elif num % 3 == 0:
        print ('Fizz')
    elif num % 5 == 0:
        print ('Buzz')
    else:
        print(num)

        


# In[112]:


# 4. Display a table of powers.

# -Prompt the user to enter an integer.
# -Display a table of squares and cubes from 1 to the value entered.
# -Ask if the user wants to continue.
# -Assume that the user will enter valid data.
# - Only continue if the user agrees to.

# Example Output

'''
What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125
'''


            
end = int(input("What number would you like to go up to? "))

print("\nHere is your table!\n")

for x in range(1, end + 1):
            print(x, x ** 2, x ** 3)


# In[ ]:


# Bonus: Research python's format string specifiers to align the table


# In[110]:


# 5. Convert given number grades into letter grades.

# -Prompt the user for a numerical grade from 0 to 100.
# -Display the corresponding letter grade.
# -Prompt the user to continue.
# -Assume that the user will enter valid integers for the grades.
# -The application should only continue if the user agrees to.

'''
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
'''
number_grade = int(input('Enter a numerical grade from 0 to 100: '))

user_continue = True

while user_continue == True:
    if number_grade in range(88,101):
        print ('Letter grade = A\n')
    elif number_grade in range(80,88):
        print ('Letter grade = B\n')
    elif number_grade in range(67,80):
        print ('Letter grade = C\n')
    elif number_grade in range(60,67):
        print ('Letter grade = D\n')
    else:
        print ('Letter grade = F\n')
    x = input('Would you like to continue? Type yes/no: ')
    if x == 'yes':
        user_continue = True
        number_grade = int(input('\nEnter a numerical grade from 0 to 100: '))        
    else:
        user_continue = False
    
# Bonus

# -Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).


# In[127]:


# 6. Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre.
# Loop through the list and print out information about each book.

books = [
    {
        "title": "Genetic Algorithms and Machine Learning for Programmers",
        "genre": 'Programming',
        "author": "Frances Buontempo"
    },
    {
        "title": "The Visual Display of Quantitative Information",
        "genre": 'Math/Science',
        "author": "Edward Tufte"
    },
    {
        "title": "Practical Object-Oriented Design",
        "author": "Sandi Metz",
        "genre": 'Programming'
    },
    {
        "title": "Weapons of Math Destruction",
        "author": "Cathy O'Neil",
        "genre": 'Nonfiction'
    }
]

for index in range(len(books)):
    for key in books[index]:
        print (books[index][key])
    print('\n')    


# In[154]:


# a. Prompt the user to enter a genre, 
# then loop through your books list and print out the titles of all the books in that genre.

genre_entry = input('Enter a Genre: ')
print (f'\nBooks under "{genre_entry}":')

for index in range(len(books)):
    if genre_entry == books[index]['genre']:
        print (books[index]['title'])  

    

