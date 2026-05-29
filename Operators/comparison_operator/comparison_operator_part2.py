## SECTION 2: COMPARISON OPERATORS ( == != > < >= <= )
# 30 Questions

# 11. Take username and check if it equals "Sagar".
# 12. Take a number and check if it is positive.
# 13. Take a number and check if it is negative.
# 14. Take two numbers and check if first is less than or equal to second.
# 15. Take price and check if it is greater than 1000.
# 16. Take two strings and compare if they are equal.
# 17. Take a number and check if it is exactly 100.
# 18. Take age and check if age is not 60.
# 19. Take two numbers and check which one is bigger.
# 20. Take exam score and check if score >= 90.



# 11. Take username and check if it equals "Sagar".
username = input('enter your username :-')
name = str(input("enter your name :- "))
if username == "vansh_patel":
    print("username is correct")
    
    if name == "vansh":
        print("name is correct")
    else:
        print("name is not corrrect")
else:
    print("your username is not correct")
    
'''
enter your username :-vansh_patel
enter your name :- vansh
username is correct
name is correct

'''


# 12. Take a number and check if it is positive.
number = int(input("enter your positive number :- "))
if number > 0:
    print("positive number")
else:
    print("the number is negative")
    
    
'''
enter your possitive number :- 12
positive number
------------------------------------------------
enter your positive number :- -12
the number is negative
'''
    

# 13. Take a number and check if it is negative.
number = int(input("enter your negative number :- "))
if number < 0:
    print("the number is negative")
    
else:
    print("the number is positive")

'''
enter your negative number :- -12
the number is negative
-----------------------------------------------
enter your negative number :- 12
the number is positive
'''


# 14. Take two numbers and check if first is less than or equal to second.
num1 = int(input("enter the number 1 :- "))
num2 = int(input("enter the number 2 :- "))

if num1 <= num2:
    print(f"{num1} is less than or equal to {num2}")
 
else:
    print(f'{num1} is greater than {num2}') 


'''
enter the number 1 :- 12
enter the number 2 :- 12
the number are equal
-------------------------------------
enter the number 1 :- 12
enter the number 2 :- 13
the 12 is lower than 13

'''   

# 15. Take price and check if it is greater than 1000.
price = int(input("enter the price :- "))
if price > 1000:
    print(f"the {price} are greater than 1000")
    
else:
    print(f"the {price} less than 1000 ")
    
'''
enter the price :- 20000
the 20000 are greater than 1000

-----------------------------

enter the price :- 200
the 200 less than 1000 
'''

# 16. Take two strings and compare if they are equal.
name1 = str(input("enter the 1st name :- "))
name2 = str(input("enter the 2nd name :- "))

if name1 == name2:
    print(f"the {name1} are same {name2}")

else:
    print(f"the {name1} are greter than {name2}")
    
'''
enter the 1st name :- sam 
enter the 2nd name :- sam
the sam are same sam

---------------------------------

enter the 1st name :- vansh
enter the 2nd name :- sam
the vansh are greter than sam
'''

# 17. Take a number and check if it is exactly 100.
number1 = int(input("enter your number :- "))
if number1 == 100:
    print(f'the {number1} exactly 100')

else:
    print(f'the {number1} are not exact match')

'''
enter your number :- 100 
the 100 exactly 100
----------------------------
enter your number :- 200
the 200 are not exact match
'''


# 18. Take age and check if age is not 60.
age = int(input("enter your age :- "))

if age != 60:
    print('the age not 60')
    
else:
    print("the age is 60")
    
'''
enter your age :- 23
the age not 60
-------------------------
enter your age :- 60
the age is 60
'''

# 19. Take two numbers and check which one is bigger.
number1 = int(input("enter your 1st number :- "))
number2 = int(input("enter your 2nd number :- "))

if number1 > number2:
    print(f"the {number1} are the bigger of {number2}")
    
elif number1 < number2:
    print(f"the {number1} are smaller of {number2}")
     
else:
    print(f"the {number1} and {number2 } are euqal")

'''
enter your 1st number :- 23
enter your 2nd number :- 12
the 23 are the bigger of 12
-------------------------------

enter your 1st number :- 13
enter your 2nd number :- 34
the 13 are smaller of 34

------------------------------
enter your 1st number :- 12
enter your 2nd number :- 12
the 12 and 12 are euqal

'''

# 20. Take exam score and check if score >= 90.

marks = int(input("enter your marks:- "))

if marks >= 90:
    print("A+")
    
elif marks >= 80:
    print("B+")
    
elif marks >= 70:
    print("C+")
    
elif marks >= 50:
    print("D")
    
elif marks >= 40:
    print("E")
    
else:
    print("FAIL")
    

# 20. Take exam score and check if score >= 90.
marks = int(input("enter your marks:- "))
if marks > 90:
    print(f"the {marks} marks are greter than 90")
else:
    print(f"the {marks} marks are the less than 90")




