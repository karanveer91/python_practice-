'''
### Basic Level (1-15)

1. Take a number and check if it is positive, negative, or zero.
2. Take a number and check if it is even or odd.
3. Take age and print:
    - "Child" if age < 13
    - "Teen" if age 13-19
    - "Adult" otherwise
    
4. Take marks and print:
    - "Fail" if < 35
    - "Pass" if 35-59
    - "First Class" if 60-79
    - "Distinction" if 80+
    
5. Take temperature and print:
    - "Cold" if < 15
    - "Warm" if 15-30
    - "Hot" if > 30
    
6. Take salary and classify:
    - Low (< 30000)
    - Medium (30000-70000)
    - High (> 70000)
    
7. Take a number and check if it is divisible by 3, 5, or both.
8. Take two numbers and print which one is greater or if equal.
9. Take a character and check if it is a vowel or consonant.
10. Take a year and check if it is leap year or not.
11. Take a number and check if it is 1-digit, 2-digit, or 3-digit.
12. Take exam score and print grade (A, B, C, D, F).
13. Take a number and check if it lies between 10 and 50.
14. Take username and check:
    - "admin" → Admin Access
    - "guest" → Guest Access
    - otherwise → Invalid User
15. Take password and check if it matches "python123".

'''


# 1 Take a number and check if it is positive, negative, or zero.

number = int(input("enter your number :- "))

if number > 0:
    print("the number are positive")
    
elif number < 0:
    print("the number are negative")

else:
    print("the number are zero")
    
    
'''
enter your number :- 12
the number are positive
------------------------------
enter your number :- -12
the number are negative
------------------------------
enter your number :- 0
the number are zero

'''


# 2 Take a number and check if it is even or odd.

number = int(input("enter your number :- "))

if number % 2 == 0:
    
    print("the number are EVEN")


else:
    print("the number are ODD")

'''
enter your number :- 12
the number are EVEN
------------------------------
enter your number :- 13
the number are ODD
'''

    
'''
3. Take age and print:
- "Child" if age < 13
- "Teen" if age 13-19
- "Adult" otherwise

'''

age = int(input("enter your age :- "))

if age <= 13:
    print("the age is child")
    
elif age <= 19:
    print("the age is teen")
    
else:
    print("the age is Adult")


'''
enter your age :- 10
the age is child
------------------------------
enter your age :- 19
the are is teen
------------------------------
enter your age :- 20
the age is Adult
'''




'''
# 4. Take marks and print:
- "Fail" if < 35
- "Pass" if 35-59
- "First Class" if 60-79
- "Distinction" if 80+

'''


marks = int(input("enter your marks :- "))

if marks >= 80:
    print("distination gread (a+)")
    
elif marks >= 60:
    print("First class")
    
elif marks >= 35:
    print("pass")
    
else:
    print("try next sem")



'''
"5. Take temperature and print:
- "Cold" if < 15
- "Warm" if 15-30
- "Hot" if > 30
   
'''

temperature = float(input("enter the temperature :- "))

if temperature < 15:
    print("the temperature are COLD")
    
elif temperature <= 30:
    print("the temperature are WARM")
    
else:
    print("the temperature are HOT ")


'''
enter the temperature :- 10
the temperature are COLD
------------------------------
enter the temperature :- 17
the temperature are WARM
------------------------------
enter the temperature :- 36
the temperature are HOT 

'''


'''
6. Take salary and classify:
    - Low (< 30000)
    - Medium (30000-70000)
    - High (> 70000)
'''


salary = int(input("enter your salary :- "))

if salary < 30000:
    print("the salary are LOW")

elif salary <= 70000:
    print("the salary are MEDIUM")
    
else:
    print("The salary are HIGH")


'''
enter your salary :- 20000
the salary are LOW
------------------------------
enter your salary :- 50000
the salary are MEDIUM
------------------------------
enter your salary :- 100000
The salary are HIGH
'''




# 7 Take a number and check if it is divisible by 3, 5, or both.

number = int(input("enter your number :- "))
if number % 3 == 0 and number % 5 == 0:
    print("the number are divisible to both 3 and 5")
    
elif number % 3 == 0:
    print("the number are divisible 3")
    
elif number % 5 ==0:
    print("the number are  divisible 5")


else:
    print("the number are not divisible")

'''
enter your number :- 12
the number are divisible 3
------------------------------
enter your number :- 20
the number are  divisible 5
------------------------------
enter your number :- 14
the number are not divisible

'''


# 8 Take two numbers and print which one is greater or if equal.

number1 = int(input("enter your 1st number :- "))
number2 = int(input("enter your 2nd number :- "))

if number1 > number2:
    print(f"the {number1} are greter than {number2} ")
    
elif number1 < number2:
    print(f"the {number1} are less than {number2 }")
    
else:
    print(f"the {number1} and {number2} are equal")


'''

enter your 1st number :- 35
enter your 2nd number :- 12
the 35 are greter than 12 
------------------------------
enter your 1st number :- 12
enter your 2nd number :- 35 
the 12 are less than 35
------------------------------
enter your 1st number :- 12
enter your 2nd number :- 12
the 12 and 12 are the equal

'''









#9 Take a character and check if it is a vowel or consonant.

character = input("enter your charecter name :- ")

if character.lower() in  "aeiou":
    print("the charecter are vowel")
    
else:
    print("the charecter are consonant")



#------------------------------------------------------------------------------

character = input("enter your character :- ")

if character.isalpha():
    if character.lower() in "aeiou":
        print("It is a vowel")
    else:
        print("It is a consonant")
else:
    print("Invalid input")
    
    
    
    
    
    
    
#12 take exam score and print grade (A, B, C, D, F).

marks = int(input("enter your marks :- "))

if marks >= 90:
    print("grade A")
    
elif marks > 80:
    print("gread B")
    
elif marks > 60:
    print("gread C")

elif marks > 45:
    print("gread D")
    
else:
    print("you are Fail")