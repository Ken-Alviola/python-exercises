'''You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it),
 and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
'''
little_mermaid = 3
brother_bear = 5
Hercules = 1
price_per_day = 3

total = little_mermaid * price_per_day + brother_bear * price_per_day + Hercules * price_per_day
total

'''
Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week?
You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
'''
goog_rate = 400
amzn_rate = 380
face_rate = 350

total_pay = face_rate * 10 + goog_rate * 6 + amzn_rate * 4
total_pay

'''
A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
'''
is_not_full = True
schedule_conflict = False
is_enrolled = False

if is_not_full == True and schedule_conflict == False:
    is_enrolled = True

is_enrolled

'''
A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace
'''