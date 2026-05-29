"""
## SECTION 3: LOGICAL OPERATORS ( and or not )
30 Questions

# 1. Take age and check if age > 18 and age < 60.
# 2. Take marks and check if marks >= 35 and marks <= 100.
# 3. Take salary and check if salary > 30000 and experience > 2.
# 4. Take two numbers and check if both are positive.
# 5. Take a number and check if it is between 10 and 50.
# 6. Take username and password and validate both.
# 7. Take age and check if age < 18 or age > 60.
# 8. Take marks and check if marks < 35 or marks > 100.
# 9. Take temperature and check if temp > 40 or temp < 0.
# 10. Take two numbers and check if at least one is negative.

"""


# 1. Take age and check if age > 18 and age < 60.

age = int(input("enter your age :- "))

if age >= 18 and age <= 60: #output:- true
    print("the are are perfact")

else:
    print("they are not valid")

    
'''
enter your age :- 20
the are are perfact
-----------------------------
enter your age :- 18
they are euqal

'''


# 2. Take marks and check if marks >= 35 and marks <= 100.






# 3. Take salary and check if salary > 30000 and experience > 2.









# 4. Take two numbers and check if both are positive.









# 5. Take a number and check if it is between 10 and 50.









# 6. Take username and password and validate both.









# 7. Take age and check if age < 18 or age > 60.









# 8. Take marks and check if marks < 35 or marks > 100.

marks = int(input("enter your marks :- "))

if marks > 90:
    print('A+++')
    
elif marks < 35:
    print("the marks are less than 35")
    
'''
enter your marks :- 95
A+++
------------------------------
enter your marks :- 23
the marks are less than 35
'''

# 9. Take temperature and check if temp > 40 or temp < 0.

temperture = float(input("enter your your temperture :- "))
if temperture > 40:
    print("the temperture are hot")
    
elif temperture < 0:
    print("the temperture are the minus degree ")

else:
    print("the temperture are equal")

'''
enter your your temperture :- 45
the temperture are hot
------------------------------
enter your your temperture :- -23
the temperture are the minus degree 

------------------------------
enter your your temperture :- 40
the temperture are equal

'''   


# 10. Take two numbers and check if at least one is negative.

number1 = int(input("enter your 1st number :- "))
number2 = int(input("enter your 2nd number :- "))

if number1 > 0 or number2 < 0:
    print("the at least one number are negative")

else:
    print("the both number are negative")

'''
enter your 1st number :- 10
enter your 2nd number :- -5
the at least one number are negative

------------------------------

enter your 1st number :--5
enter your 2nd number :-10

the both number are negative

'''





