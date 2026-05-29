"""
## SECTION 1: ARITHMETIC OPERATORS ( + - * / // % ** )
30 Questions

1. Take two integers from user and print their sum.
2. Take two integers and print subtraction result.
3. Take two floats and print multiplication result.
4. Take two numbers and print division result.
5. Take two integers and print floor division result.
6. Take two integers and print remainder using %.
7. Take a number and print its square using **.
8. Take a number and print its cube.
9. Take two numbers and calculate average.
10. Take length and width from user and calculate area.
11. Take radius and calculate area of circle (3.14 * r * r).
12. Take principal, rate, time and calculate simple interest.
13. Take total marks of 5 subjects and calculate percentage.
14. Take salary and increase it by 10%.

---------------Start part 2---------------------------------------
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
    
# 1. Take two integers from user and print their sum.
User_one = int(input("enter number of sum:- "))
User_two = int(input("enter number of sum:- "))
result = User_one + User_two
print("sum is", result)

'''
enter number of sum:- 3
enter number of sum:- 3
output:- sum is 6

'''

#2. Take two integers and print subtraction result.
user_one = int(input("enter number to subtraction:- "))
user_two = int(input("enter number to subtraction:- "))
result = user_one - user_two
print("subtraction:-", result)

'''
enter number to subtraction:- 3
enter number to subtraction:- 3
output:- subtraction:- 0
'''

#3. Take two floats and print multiplication result.

user_one = float(input("enter number to multiplication:- "))
user_two = float(input("enter number to multiplication:- "))
result = user_one * user_two 
print("multiplication:-", result)

'''
enter number to multiplication:- 3
enter number to multiplication:- 3
output:- multiplication:- 9

'''

#6. Take two integers and print remainder using %.
user_one = int(input("enter number to remainder:-"))
user_two = int(input("enter number to remainder:-"))
result = user_one % user_two
print("remainder:-", result)

"""
nter number to remainder:-9
enter number to remainder:-3
remainder:- 0
"""

#7. Take a number and print its square using **.
user_one = int(input("enter number to square :-"))

result = user_one ** 2
print("square",result)

"""
enter number to square :-12
enter number to square :-3
output :- square 1728

"""

#9. Take two numbers and calculate average.
user_one = int(input("enter number of average :- "))
user_two = int(input("enter number of average :- "))
average = (user_one + user_two) / 2  
print("avegare :- ", average)
   
"""
enter number :- 23
enter number:- 45
output:-  avegare :-  34.0
-------------------------------------------
📊 Full Flow Diagram

User enters → 23
User enters → 45

23 + 45 = 68
68 / 2 = 34.0

Output:
avegare :- 34.0  #agr 0 nahi chahiye honga to hum use karenge // 2  ex:- average = (user_one + user_two) // 2  
-------------------------------------------------
Line 3 (Average Formula)
average = (user_one + user_two) / 2

"""

#8. Take a number and print its cube.

number = int(input("Enter number and and calculate the cube :- "))
cube = number * number * number  # cube = number ** 3
print("Cube is:", cube)

"""
Enter number: 3
Cube is: 27
--------------------------------------
Cube ka matlab hota hai:

formula:-

Cube = number * number * number
Example:
cube = 3 * 3 * 3 = 27
"""


#10. Take length and width from user and calculate area.

user_one = int(input("enter length and calculate the area :- "))
user_two = int(input("enter width and calculate the area :- "))
area = (user_one * user_two)
print("area", area)

"""
enter number and calculate the area :- 12
enter number and calculate the area :- 5
output :-  area 60
------------------------------------------------------
Step-by-Step (Baby Explanation)
1️⃣ Length input
user_one = int(input("enter length and calculate the area :- "))

User input deta hai:

12

Ab variable me store ho gaya:

user_one = 12
2️⃣ Width input
user_two = int(input("enter width and calculate the area :- "))

User input deta hai:

5

Ab variable me store ho gaya:

user_two = 5
3️⃣ Area calculate
area = (user_one * user_two)

Calculation:

12 × 5 = 60

Ab:

area = 60
4️⃣ Print output
print("area", area)

Output:

area 60
"""

#11. Take radius and calculate area of circle (3.14 * r * r).
user_one = float(input('enter redius and calculate the cricle :- '))
circle = 3.14 * user_one * user_one
print("circle", circle)

"""
enter redius and calculate the cricle :- 12
output :- circle 452.15999999999997
__________________________________________________________

Step-by-Step Explanation
1️⃣ Radius input lena
radius = float(input("Enter radius: "))
input() → user se value leta hai
float() → decimal number allow karta hai

Example user input:

Enter radius: 5

Ab variable me store hoga:

radius = 5
2️⃣ Area calculate karna
area = 3.14 * radius * radius

Calculation:

3.14 * 5 * 5
5 * 5 = 25
3.14 * 25 = 78.5

Ab:

area = 78.5
3️⃣ Output print karna
print("Area of circle:", area)

Output:

Area of circle: 78.5
"""

#14. Take salary and increase it by 10%.
user_one = float(input("enter salary number and the calculate the. salary on 10%:- "))
new_salary = user_one + (user_one * 10 /100)
print("salary", new_salary)

"""
Step-by-Step (Baby Explanation)

1 Salary input lena
user_one = float(input("enter salary number and the calculate the. salary on 10%:- "))

Example user input:

20000

Ab variable me store ho gaya:

user_one = 20000
 
 10% calculate karna
user_one * 10 / 100

Calculation:

20000 × 10 = 200000
200000 / 100 = 2000

Matlab 10% increase = 2000

3 New salary calculate karna
new_salary = user_one + (user_one * 10 /100)

Calculation:

20000 + 2000 = 22000

Ab:

new_salary = 22000
4 Output print
print("salary", new_salary)

Output:

salary 22000

"""

#12. Take principal, rate, time and calculate simple interest.
money = int(input("enter initial money :- "))
rate = int(input("enter Interest rate(%) :- "))
time = float(input("enter time/years :-  "))

calculate_simple_interest = (money * rate * time) /100
print("simple interest", calculate_simple_interest)

"""
Step-by-Step Example

User input:

enter initial money :- 10000
enter Interest rate(%) :- 5
enter time/years :- 2
1:- Variables me values store
money = 10000
rate = 5
time = 2
2:- Formula apply
SI = (10000 * 5 * 2) / 100

Step calculation:

10000 * 5 = 50000
50000 * 2 = 100000
100000 / 100 = 1000
3:- Output
simple interest 1000

✅ Result correct hai.

"""

#15. Take a number and divide it by 2 using /= operator.
User_one = int(input("divide the number :- "))
User_one /= 2
print("result",User_one)

"""
Baby Step Explanation
1:- User input
User_one = int(input("divide the number :- "))

Example user input:

divide the number :- 20

Ab variable me store ho gaya:

User_one = 20
2:- /= operator use
User_one /= 2

Iska matlab:

User_one = User_one / 2

Calculation:

20 / 2 = 10.0

Ab:

User_one = 10.0
3:- Output print
print("result",User_one)

Output:

result 10.0

"""

#13. Take total marks of 5 subjects and calculate percentage.
marathi = float(input("enter subjects mark (marathi) :- "))
hindi = float(input("enter subjects mark (hindi) :- ")) 
english = float(input("enter subjects mark (english) :- "))
science = float(input("enter subjects mark (science) :- "))
history = float(input("enter subjects mark (history) :- "))
total_subjects =  marathi + hindi + english + science + history
percentage = (total_subjects / 500) * 100
print("percentage", percentage)



#take a number and multiply it by 5 using *= operator.
User_one = int(input("enter number and calculate using (*=) operator :- "))
user_one *= 5
print("result", user_one)





