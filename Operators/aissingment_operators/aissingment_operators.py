"""
## SECTION 1: ASSIGNMENT OPERATORS
( = += -= *= /= //= %= **= )
30 Questions

1. Create a variable x = 10 and print it.
2. Take a number from user and assign it to variable num. Print num.
3. Create x = 5. Increase x by 3 using +=. Print result.
4. Create salary = 50000. Increase it by 10000 using +=.
5. Create marks = 80. Reduce it by 5 using -=.
6. Take a number and double it using *=.
7. Take a float number and divide it by 2 using /=.
8. Create x = 25. Apply //= 4. Print result.
9. Create x = 29. Apply %= 5. Print remainder.
10. Create x = 2. Apply **= 3. Print result.

"""

#1. Create a variable x = 10 and print it.
number = 10
print(number) #output:- 10

#2. Take a number from user and assign it to variable num. Print num.

number = int(input("enter your number :- "))

print(number)

'''
enter your number :- 10
10
'''

#3. Create x = 5. Increase x by 3 using +=. Print result.
number = 5
number += 3
print(number) #output :- 8


#4. Create salary = 50000. Increase it by 10000 using +=.

salary = 5000
salary += 1000

print(salary) #output :- 6000


#5. Create marks = 80. Reduce it by 5 using -=.

Marks = 80
Marks -= 5
print(Marks) #output:- 75


#6. Take a number and double it using *=.

number = int(input("enter your number :- "))
number *= 2
print(number)

'''
enter your number :- 5
10
-----------------------------
enter your number :- 3
6
'''

#7. Take a float number and divide it by 2 using /=.

number = float(input("enter your number :- "))
number /= 2
print(number)

'''
enter your number :- 5
2.5
-----------------------
enter your number :- 23
11.5
'''

#8. Create x = 25. Apply //= 4. Print result.
number = 25
number //= 4
print(number)



#Create x = 29. Apply %= 5. Print remainder.

number = 20
number %= 5
print(number) #output:- 0

#10. Create x = 2. Apply **= 3. Print result.

Number = 4
Number **= 3
print(Number) #output:- 64


#Take two numbers a and b. Add b into a using +=.

a = int(input("enter your 1st number :- "))
b = int(input("enter your 2nd number :- "))

a += b

print(a)

'''
enter your 1st number :- 12
enter your 2nd number :- 12
24

'''

#Take price = 1000. Apply 10% discount using -=.

price = int(input("enter your price :- "))
Discount = 10
# formula 1st :- price - (price * discount / 100) 

# formula 2nd :- Final Price = Price × (100 − Discount%) / 100

Final_price = price * (100 - Discount) /100

print(Final_price)

'''
enter your price :- 500
450.0

'''

#------------------------------------------------------

price = int(input('enter yoyr price :- '))
discount = 10
new_discount = price * discount / 100
price -= new_discount
print(price)

'''
enter yoyr price :- 500
450.0

'''

