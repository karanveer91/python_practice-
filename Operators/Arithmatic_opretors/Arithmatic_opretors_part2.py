"""
15. Take a number and divide it by 2 using /= operator.
16. Take a number and multiply it by 5 using *= operator.
17. Take two numbers and swap them using arithmetic operators.
18. Take a number and check if it is even using %.

20. Take total seconds and convert into minutes (use // and %).
21. Take temperature in Celsius and convert to Fahrenheit.
22. Take two numbers and print their power result.
23. Take price and discount %, calculate final price.
24. Take a 3-digit number and find sum of digits using % and //.
25. Take two numbers and print remainder without using % (use formula).
26. Take a number and print half of it.
27. area of triangle.27. Take base and height and calculate 
28. Take a number and print its square root using ** 0.5.
29. Take monthly salary and calculate yearly salary.
30. Take total bill and number of people, calculate per person share.

"""

#15. Take a number and divide it by 2 using /= operator.

user_one = float(input("enter number to calculate the divide operator :- "))
user_one /= 2
print("result", user_one)

"""
Example Run

Input:

Enter number: 20

Calculation:

20 / 2 = 10

Output:

Result: 10.0
_______________________________________________________

/= Operator Meaning
x /= 2

Same as:

x = x / 2

Example:

x = 8
x /= 2

Result:

4.0
"""



#16 take a number and multiply it by 5 using *= operator.
user_one = int(input("enter number and calculate using (*=) operator :- "))
user_one *= 5
print("result", user_one)

"""
Step by Step Example

User input:

enter number :- 10

Program:

user_one = 10
user_one *= 5

Calculation:

10 * 5 = 50

Output

result 50

 """


#17. Take two numbers and swap them using arithmetic operators.

user_one = int(input("enter the first and the swap the number :- "))
user_two = int(input("enter the second and the swap the number :- "))
user_one,user_two = user_two,user_one
print("value_1:- ",user_one)
print("value_2:- ",user_two)

'''
enter the first and the swap the number :- 12
enter the second and the swap the number :- 2
swap output :- value_1:-  2
swap output :- value_2:-  12
'''

#18. Take a number and check if it is even using %.
user_one = int(input("enter the number and check number ODD OR EVEN :- "))
if user_one % 2 == 0:
    print("EVEN") #AGR 0 BACH RHA HAI TO EVEN HAI
else:
    print("ODD") #AGR 1 BACH. RAHA HAI TO ODD HAI
    
    
#20. Take total seconds and convert into minutes (use // and %).
second = int(input("enter second :- "))

Minutes = second // 60   #// → full minutes nikalta hai

Remaining_second = second % 60    #% → remaining seconds batata hai
print("convert second to minutes",Minutes)

"""
enter second :- 60
convert second to minutes 1.0
------------------------------------------------------
Example 1

Input

enter second :- 60

Calculation

60 // 60 = 1 minute
60 % 60 = 0 second

Output

minutes: 1
remaining seconds: 0
Example 2

Input

enter second :- 125

Calculation

125 // 60 = 2 minutes
125 % 60 = 5 seconds

Output

minutes: 2
remaining seconds: 5
✔ Simple Formula
minutes = seconds // 60
seconds = seconds % 60

// → full minutes nikalta hai
% → remaining seconds batata hai

"""


#21. Take temperature in Celsius and convert to Fahrenheit.
Celsius = float(input("enter the number and count the temperature :- "))

#FORMULA :- F = (C × 9/5) + 32 

Fahrenheit = (Celsius * 9/5) + 32

print(f"the temperature is {Fahrenheit}°C")

'''
Step by Step Example

User input:

enter temperature in celsius :- 25

Calculation:

25 × 9/5 = 45
45 + 32 = 77

Output:
temperature in fahrenheit :- 77.0

4 Code Breakdown

User Input
celsius = float(input("enter temperature in celsius :- "))

User se temperature liya.

Conversion Formula
fahrenheit = (celsius * 9/5) + 32

Celsius ko formula se Fahrenheit me convert kiya.

Output
print("temperature in fahrenheit :-", fahrenheit)

Result screen par print kiya.

enter the number and count the temperature :- 34
the temperature is 93.2°C
'''


# 22. Take two numbers and print their power result.
user_one = int(input('enter the  (first) number and calculate the number to the power :- '))
user_two = int(input('enter the (second) number and calculate the number  the power :- '))
result = user_one ** user_two
print("power", result) 

"""
enter the  (first) number and calculate the number to the power :- 2
enter the (second) number and calculate the number  the power :- 4
power 279841
"""


#23 take price and discount %, calculate final price.
user_one = int(input("enter the price :- "))
user_two = float(input("enter the discont % :- "))

# Formula
# final_price = price - (price × discount / 100)

result  = user_one - (user_two * 10 / 100)

print("discount", result)

'''
enter the price :- 2000
discount 1800.0
-----------------------------------
Example Run

Input

enter price :- 2000
enter discount % :- 10

Calculation

discount = 2000 * 10 / 100
discount = 200

Final price

2000 - 200 = 1800

Output

final price :- 1800.0

'''

#24 Take a 3-digit number and find sum of digits using % and //.
user_one = int(input("enter the 3 number :- "))

digits1 = user_one % 10
number = user_one // 10

digits2 = user_one % 10
number = user_one // 10

digits3 = user_one % 10

result = digits1 + digits2 + digits3

print("sum digits result", result)


'''
✔ Step-by-Step Example

Input

enter 3 digit number :- 123
Step 1 → Last digit
123 % 10 = 3

So

digit1 = 3
Step 2 → Remove last digit
123 // 10 = 12

Now number becomes

12
Step 3 → Second digit
12 % 10 = 2

So

digit2 = 2
Step 4 → Remove second digit
12 // 10 = 1
Step 5 → Third digit
1 % 10 = 1

So

digit3 = 1
✔ Final Sum
digit1 + digit2 + digit3
3 + 2 + 1 = 6

Output

sum of digits :- 6
'''

# 25. Take two numbers and print remainder without using % (use formula).
user_one = int(input("enter 1st number"))
user_two = int(input("enter 2nd number"))

result = user_one - (user_one // user_two) * user_two

# Remainder ka Formula
# remainder = dividend - (divisor * quotient)
# emainder = a - (a // b) * b

print("result", result)

'''
Example

Input

enter first number :- 17
enter second number :- 5

Step 1

17 // 5 = 3

Step 2

3 * 5 = 15

Step 3

17 - 15 = 2

Output

remainder :- 2
✔ Simple Breakdown
a // b  → quotient
quotient * b → total divisible part
a - divisible part → remainder

Example

17 ÷ 5
5 × 3 = 15
17 - 15 = 2

So remainder = 2

💡 Interview Trick

remainder = a - (a // b) * b

Ye % operator ka formula version hai.
'''

#27. area of triangle.27. Take base and height and calculate 
height = float(input("enter your height :- "))
base = float(input("enter your base  :- "))

#formula :- area = (base * height) / 2

area = (base * height) / 2
print(f'area of the trangle {area}')

'''
enter your heigt :- 5.5
enter your base  :- 10
area of the trangle 27.5

'''


#28. Take a number and print its square root using ** 0.5.

import math
num = int(input("enter your number :- "))

result = math.sqrt(num)
print



#28. Take a number and print its square root using ** 0.5.
import math

num = int(input('enter your numbwer :- '))

result = math.sqrt(num)
print("root", result)

'''
enter your numbwer :- 12
root 3.4641016151377544
'''

#   ----------------both are same -------------------------

num = float(input("enter your number :- "))
square_root = num ** 0.5
print('square root :- ', square_root)

'''
enter your number :- 12
square root :-  3.4641016151377544
'''


#29. Take monthly salary and calculate yearly salary.

month_salary = int(input("enter your monthly salary :- "))

#formula:- year_salary = (month_salary * 12)

year_salary = (month_salary * 12)

print(f'year salary is {year_salary} LPA')


'''
enter your monthly salary :- 10000
year salary is 120000 LPA
'''


#30. Take total bill and number of people, calculate per person share.

total_bill = int(input("enter total bill :- "))
total_person = int(input("enter total people :- "))

#formula:- per_person_share = Total Bill / Number of People

per_person_share = total_bill /  total_person

print('per_person share' , per_person_share)

'''
enter total bill number :- 209
per_person share 10.45

'''




