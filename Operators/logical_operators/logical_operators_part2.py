'''
## SECTION 3: LOGICAL OPERATORS ( and or not )
30 Questions

11. Take number and check if it is not zero.
12. Take age and check if not (age < 18).
13. Take a number and check if it is even and greater than 10.
14. Take salary and check if salary > 50000 or department == "IT".
15. Take two strings and check if both are equal and not empty.
16. Take number and check if it is divisible by 3 and 5.
17. Take number and check if it is divisible by 3 or 5.
18. Take marks and check if marks >= 90 or marks < 40.
19. Take password and check if it is not "1234".
20. Take two numbers and check if both are not equal to zero.

'''

#Take number and check if it is not zero.

number1 = int(input("enter your number :- "))


if number1 != 0:
    print("the number are not equal to zero")
      
else:
    print("the number are the equal to zero")




#Take a number and check if it is even and greater than 10.
number = int(input("enter your number :- "))

if number % 2 == 0 and number > 10:
    print("the number are even and also the number are the greater than")
    
elif number % 2 == 0:
    print("the number are EVEN number but not greater")
    
elif number > 10:
    print("the number not EVEN but is greater than 10")
    
else:
    print("the numberis ODD number and the number are smallest")



#14. Take salary and check if salary > 50000 or department == "IT".
# salary = int(input('enter your salary :- '))
# departmnet = input("enter your department :- ")
# if salary > 50000:
#     if departmnet == "it":
#         print("the department are true")
        
#     else:
#         print("the department are invalide")
# else:
#     print("the salary are less than 50000")

#---------------------------------------------------


# salary = int(input("enter your salary :- "))
# if salary > 50000 or departmnet == "it":
#     print("the conditions are ture ")

# else:
#     print("the condition are flase ")














