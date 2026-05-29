"""
LEVEL 2 — Multiple Variables (26--50)

x, y, z = 10, 20, 30 assign kare.
a = b = c = 100 assign kare.
first_name, last_name bana kar full name print kare.
num1, num2 ka multiplication store kare.
length, width bana kar area store kare.
price, quantity bana kar total price store kare.
marks1, marks2, marks3 ka average store kare.
x = 10 ko update karke 20 kare.
a = 10 aur b = 5 ka difference store kare.
salary variable ko 10% increase kare.
age variable ko 1 year increase kare.
x = 5 aur y = 2 ka division store kare.
num = 50 variable ko num = num + 10 kare.
num = num - 5 kare.
num = num * 2 kare.
num = num / 4 kare.
first = "Hello" aur second = "World" join kare.
x = 10, y = "10" ka type check kare.

"""
#x, y, z = 10, 20, 30 assign kare.
x ,y, z = 10, 20, 30
print(x, y, z) #output:- 10 20 30


#a = b = c = 100 assign kare.
a = 100
b = a
c = b
print(a, b, c) #output:- a=100  b=100  c=100


#first_name, last_name bana kar full name print kare.
name = "sandip"
last_name = "patil"
print(name, "" + last_name) #output:-  sandip patil

#num1, num2 ka multiplication store kare.
num1 = 5
num2 = 5
print(num1 * num2) #output:- 25


#length, width bana kar area store kare.
lenght = 10
width = 5
area = lenght * width
print(area)  #output:- 50

#price, quantity bana kar total price store kare.
Price = 200
Quantity = 2
total = Price * Quantity
print(total)              #output:- 400

#marks1, marks2, marks3 ka average store kare.
marks1 = 50
marks2 = 70
marks3 = 90
average = (marks1 + marks2 + marks3) / 3  #Parentheses () use karna zaruri hai jab multiple operations ho.
print(average) #output:- 70

#x = 10 ko update karke 20 kare.
x = 10
x = x + 10 #ye dono hi tarike se hum likh sakte hai
x = 20     #ye dono hi tarike se hum likh sakte hai
print(x)  #output:- 20

#a = 10 aur b = 5 ka difference store kare.
a = 10
b = 5
difference = (a - b)
print(difference)  #output:- 5

#salary variable ko 10% increase kare.
salary = 10
# Increase = (salary * 10 /200)
new_salary = salary + (salary * 10 / 100)
print(new_salary)
"""
Logic

Step 1 — 10% nikalna

10 × 10 / 100 = 1

Step 2 — salary me add

10 + 1 = 11

✅ New salary = 11
"""

#age variable ko 1 year increase kare.
age = 2025
age = 2026   #direct value change
age = (age + 1)  #1 se increase karna hota hai.
print(age)  #output:- 2026

#Increase age by 1
age = 2001
age = age + 1
print(age)  #output:- 2002

#x = 5 aur y = 2 ka division store kare.
x = 5
y = 2 
z = (x / y)
print(z)    #output:- 2.5

#Update num = num + 10.
num = 10
num = (num + 10)
print(num) #output:- 20

#Update num = num - 5.
num = 10
num = (num - 5)
print(num)  #output:- 5

#Update num = num * 2.
num = 10
# num = (num * 2)
# print(num) #output:- 20   10 me add ho gaya hai 20 update ab num *= 20 se  multiple hoga or hume output:- 40 aayega

num *= 2 #Python me Short Way
print(num) #output:- real output is 20   agr num = (num * 2) to output:- 40 aayega

#Update num = num / 4.
num = 10
# num = (num / 4)
num /= 4
print(num)  #output:- 2.5

"""
explanation:-

Divide ka simple matlab

Divide ka matlab hota hai — kisi cheez ko barabar parts me baantna.

Example:

Tumhare paas 10 chocolates 🍫 hain
Aur 4 bachcho me baantni hai

To har bachche ko kitni milegi?

10 ÷ 4 = 2.5

Matlab har bachche ko 2.5 chocolate milegi.
"""
#Join first = "Hello" and second = "World".
Name = "vansh"
surname ="patil"
print(Name + surname) #output:- vanshhpatil

#Multiply a = 3 and b = 3.5.
a = 3
b = 3
multiply = (a * b)
print(multiply)  #output:- 9
# print(a * b)   #output:- 9

#Print temperature = 30.
tem = 30
print(tem) #output:- 30

#Update speed = 80.
speed = 70
speed = (speed + 10)
print(speed)   #output:-  80

#Print height = 5.9.
height = 5.5
height = (height + 0.4)
print(height) #output:- 5.9


#Store weight = 70.
weight = 70
print(weight)  #output:- 70






