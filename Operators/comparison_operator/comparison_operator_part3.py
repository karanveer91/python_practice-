'''
## SECTION 2: COMPARISON OPERATORS ( == != > < >= <= )
30 Questions

21. Take two float numbers and compare equality.
22. Take number and check if it is less than 10.
23. Take two numbers and print True if both are same.
24. Take salary and check if it is below 20000.
25. Take temperature and check if it is <= 0.
26. Take a number and check if it is not zero.
27. Take two strings and check inequality.
28. Take marks and check if marks > 50.
29. Take two numbers and check >= condition.
30. Take number and compare with 500.
'''

#21. Take two float numbers and compare equality.

number1 = float(input("enter your 1st float number :- "))
number2 = float(input("enter your 2nd float number :- "))

if number1 == number2:
    print(f"the {number1} and {number2} are equal")


else:
    print(f"the {number1} are not equal {number2}")
    
    
    
#22. Take number and check if it is less than 10.
number1 = int(input("enter your 1st number :-"))

if number1 < 10:
    print(f"the {number1} are less than 10")
    
elif number1 <= 10:
    print(f'the {number1} are equal to 10')

else:
    print(f"the {number1} is greter than 10")
    
'''
enter your 1st number :-9
the 9 are less than 10
-------------------------------
enter your 1st number :-10
the 10 are equal to 10
-------------------------------
enter your 1st number :-20
the 20 is greter than 10
'''

#23. Take two numbers and print True if both are same.

number1 = int(input("enter your 1st number :- "))
number2 = int(input("enter your 2nd number :- "))

if number1 == number2:
    print('True')
    
else:
    print("False")


'''
enter your 1st number :- 23
enter your 2nd number :- 23
True

-------------------------------
enter your 1st number :- 12
enter your 2nd number :- 23
False

'''


#24. Take salary and check if it is below 20000.

salary = int(input("enter your 1st salary :- "))

if salary < 20000:
    print(f'the {salary} salary are below to 20000')
    
elif salary == 20000:
    print(f"the {salary} salary are equal to 20000")
    
else:
    print(f"the {salary} salary are the above the 20000")
    
  
'''
enter your 1st salary :- 1000 
the 1000are below to 20000
-----------------------------------
enter your 1st salary :- 20000
the 20000 salary are equal to 20000
-----------------------------------
enter your 1st salary :- 200000
the 200000 are the above the 20000
'''


#25. Take temperature and check if it is <= 0.
temperature = float(input("enter temperature :- "))
if temperature <= 0:
      print("the temperature are cooldy")

else:
    print("the temperature are the hot")

'''
enter temperature :- -34
the temperature are cooldy

------------------------------
enter temperature :- 23
the temperature are the hot

'''

#26. Take a number and check if it is not zero.
number = int(input("enter your number :- "))
if number != 0:
    print("the number are not zero")
else:
    print("the number are zero")
    
    
    
'''
enter your number :- 1
the number are not zero

----------------------------
enter your number :- 0
the number are 0

'''



#27. Take two strings and check inequality.

name1 = input("enter your 1st name :- ")
name2 = input("enter yours 2nd name :- ")
if name1  != name2:
    print(f"the {name1} and {name2} are not equal")
    
else:
    print("the name are equal")



'''
enter your 1st name :- vansh
enter yours 2nd name :- vansh
the vansh and vansh are equal

----------------------------------
enter your 1st name :- vanswh
enter yours 2nd name :- vansh
the name are not equal
'''


#28. Take marks and check if marks > 50.


marks = int(input("enter your marks :- "))
if marks > 50:
    print(f"the {marks} are greter or equal than 50")
else:
    print("the marks are smaller than 50")


'''
enter your marks :- 60
the 60 are greter or equal than 50
--------------------------------------
enter your marks ;- 40
the marks are smaller than 50

'''



#29. Take two numbers and check >= condition.

number1 = int(input("enter your 1st number :- "))
number2 = int(input("enter your 2nd number :- "))


if number1 >= number2:
    print(f"the {number1} are greter than or equal to { number2} ")

else:
    print(f"the {number1} are lower than {number2}")

'''
enter your 1st number :- 45
enter your 2nd number :- 34
the 45 are greter than or equal to 34

------------------------------
enter your 1st number :- 23
enter your 2nd number :- 34
the 23 are lower than 34

'''

#30. Take number and compare with 500.

number = int(input("enter your number :- "))

if number == 500:
    print(f"the {number} are equal to 500")
    
elif number > 500:
    print(f"the {number} are greter than 500")
    
else:
   print(f"the {number} are smaller than 500")
    
    

'''
enter your number :- 500 
the number are equal 500
--------------------------
enter your number :- 50000
the 50000 are greter than 500
-------------------------------
enter your number :- 34
the 34 are smaller than 500

'''


