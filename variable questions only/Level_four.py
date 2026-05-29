"""
LEVEL 5 — Advanced Practice (126–175)

Take user input and store it in a variable.
Convert user input into integer.
Add two user inputs and store result.
Find average of three numbers.
Convert Celsius to Fahrenheit.
Convert Fahrenheit to Celsius.
Find maximum of two variables.
Find minimum of two variables.
Find largest among three variables.
Find smallest among three variables.
Calculate simple interest.
Calculate compound interest.
Convert kilometers to miles.
Convert seconds into hours and minutes.

______________part 2_____________

Count digits in a number.
Reverse a number.
Find last digit of a number.
Find first digit of a number.
--------------end part 2 ----------------

------------part 3 --------------------
Calculate square root.
Store a random number in a variable.
Check palindrome using variables.
Check prime number.
Calculate factorial.
Generate Fibonacci sequence.
Calculate power of a number.
Perform modulus operation.
-------------end. part. 3 ----------------------

--------------part 4 -------------------------
Calculate percentage.
Calculate grade.
Calculate profit or loss.
Calculate distance.
Calculate speed.
Calculate time.
Calculate BMI.
Area of rectangle.
Area of circle.
Perimeter of square.
Perimeter of rectangle.
Perimeter of triangle.
Count odd and even digits.
-----------end part 4 -------------------------


Sum of digits.
Multiply digits.
Find maximum digit.
Find minimum digit.
Convert decimal to binary.
Convert binary to decimal.
Convert decimal to octal.
Convert decimal to hexadecimal.
Find string length.
Convert string to uppercase.
Convert string to lowercase.
"""

#Take user input and store it in a variable.
store = input("enter your name :- ")
print(f"your name good :- {store}")#output:- your name good :- vansh


#Convert user input into integer.
user = int(input("enter your number:-"))
print(f"is your lucky number :- {user}") #output:- is your lucky number:- 20

user = input("YES OR NO:-")
new_user = "okay 👍 "
print(f"{new_user}")


#Add two user inputs and store result.
user_one = input("enter your name:-")
user_two = input("enter your name:-")
print(f"welcome to mt site :- {user_one} {user_two}") #welcome to mt site :- vansh patil


#Find maximum of two variables.
A = 30
B = 45
if (A < B):
    print(f"It is an smallest value{A}") #output:- It is an smallest value30
    if (A < B):
        print(f"is are true that perfact") #output:- is are true that perfact
    else:
        ("exit the block")
else:
    print(f"It is an maximum value {B}")
    
    
A = 65
B = 45
if (A < B):
    print(f"It is an smallest value {B}") 
    if (A < B):
        print(f"is are true that perfact") 
    else:
        ("exit the block")
else:
    print(f"It is an maximum value {A}") #output:-  It is an maximum value 65
    

#Find minimum of two variables.
x = 30
y = 65
if (x > y):
    print(f"smallest number is {y}")
else:
    print(f"smallest number is {x}") #output:-  yes is smallest number is 30
    
    

#Calculate simple interest.
a = 1000
b = 5
years = 3
calculate = (a * b * years) /100
print("simple intrest",calculate) #output:- simple intrest :- 150.0

"""
P = Principal #Principal (initial money)
R = Rate      #Interest rate (%)
T = Time      #Time (years)

-------------------------------

Principal = 1000 
Rate = 5%         
Time = 3 years.   

simple_intrest = (p * r * t) / 100

"""


#Calculate compound interest.
principal = 1000
rate = 10
time = 3
compund_intrest = principal * (1 + rate/100) ** time
print("compund_intrest",compund_intrest) #compund_intrest 1331.0000000000005
    

#Convert kilometers to miles.
Kilometers = 10
miles = 0.621371
calculate = (Kilometers * miles)
print(calculate)  #6.21371

#Convert kilometers to miles.
user_ask = float(input("enter your distance:-"))
user_ask = user_ask * miles
print(f"convert the kilometer to miles {user_ask}")  #3.106855

"""
user_input :- 15

enter your distance:-15
convert the kilometer to miles 9.320565
"""


#Convert minutes to seconds.

minutes = float(input("enter your minutes:-"))
seconds = minutes * 60
print(f"seconds {seconds}") #seconds 120.0

"""
user_input:-  2

enter your minutes:-2
seconds 120.0
"""

#convert hours to seconds.
Hours = int(input("enter your hours:-"))
seconds = Hours * 3600
print(f"seconds {seconds}")

"""
Example

Input:
Enter your hours: 2

Calculation:

2  * 3600 = 7200

Output:
Seconds: 7200
"""


#convert seconds to hours.
seconds = int(input("enter your seconds:-"))
Hours = seconds / 3600  #1hours means:- 3600
print(f"hours {Hours}") 

"""
Example code:-

User input:-
Enter seconds: 7200  #3600 seconds means :- 1(hours)

Calculation:

7200 / 3600 = 2

Output:

Hours: 2.0
"""

    







