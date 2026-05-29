"""
## SECTION 2: COMPARISON OPERATORS ( == != > < >= <= )
30 Questions

1. Take two integers and check if they are equal.
2. Take two numbers and check if first is greater than second.
3. Take age and check if age is greater than 18.
4. Take salary and check if salary is at least 50000.

6. Take marks and check if marks are less than 35.
7. Take temperature and check if it is greater than 30.
8. Take two floats and compare them.
9. Take a number and check if it is zero.
10. Take password input and check if it equals "admin".

"""
#1. Take two integers and check if they are equal.
user_one = int(input('enter the number check number equal or not :- '))
user_two = int(input('enter the number check number equal or not :- '))

if user_one == user_two:
    print(f'the number is equal {user_one} and {user_two}')
else:
    print(f'the number is not equal they are diffrent number {user_one} and {user_two}')

'''
enter the number :- 12
enter the number :- 12
the number is equal to 12 and 12
----------------------------------------------------
enter the number :- 12
enter the number :- 13
the number is not equal they are diffrent number 12 and 13

'''


# 2. Take two numbers and check if first is greater than second.
user_one = int(input("enter 1st number (greter than OR not ) :- "))
user_two = int(input("enter 2nd number (greter than OR not ) :- "))

if user_one > user_two:
    print(f"the {user_one} is greter than {user_two}")
else:
    print(f"the {user_one} is not grater than {user_two} ")
    
'''
enter the number check number equal or not :- 12
enter the number check number equal or not :- 12
the number is equal 12 and 12
---------------------------------------------------

enter 1st number (greter than OR not ) :- 5
enter 2nd number (greter than OR not ) :- 13
the 13 is lower than 5 

'''

#3. Take age and check if age is greater than 18.
age = int(input("enter your age :- "))

if age > 18:
   print(f'the {age} is grater than 18')
   
else:
    print(f'the {age} is lower than 18 ')
    
'''
enter your age :- 19
the 19 is grater than 18
-----------------------------------------

enter your age :- 16
the 16 is lower than 18 

'''  

#6. Take marks and check if marks are less than 35.
marks = int(input("enter the marks :- "))
if marks > 35:
    print('pass')
else:
    print('fail')


#8. Take two floats and compare them.
user_one = float(input("enter the 1st float value and check (equal or not ) :- "))
user_two = float(input("enter the 2nd float value and check (equal or not ) :- "))

if user_one == user_two:
    print(f"the float value is equal to {user_one} to {user_two}")
else:
    print(f"the float value is not equal to {user_one} to {user_two}")
    
'''
enter the 1st float value and check (equal or not ) :- 23.5
enter the 2nd float value and check (equal or not ) :- 23.5
the float value is equal to 23.5 to 23.5

--------------------------------------------------------

enter the 1st float value and check (equal or not ) :- 23.5
enter the 2nd float value and check (equal or not ) :- 34.6
the float value is not equal to 23.5 to 34.6

'''
    
#9. Take a number and check if it is zero.

number = int(input("enter number are the check zero OR not :- "))
if number == 0:
    print("the number are zero")
else:
    print("the number are not zero")

'''
enter number are the check zero OR not :- 23
the number are not zero
---------------------------------------------
enter number are the check zero OR not :- 0
the number are zero
'''


#10. Take password input and check if it equals "admin".

password = input("enter your password :- ")
admin = str(input("enter admin name :- "))

if password == "kranveerpatil":
    print('paswword is correct')
    
    if admin == "vansh":
        print(f"{admin} name and password {password} is correct")
    else:
        print("incorrect admin name")
else:
    print("plase corrrect password")