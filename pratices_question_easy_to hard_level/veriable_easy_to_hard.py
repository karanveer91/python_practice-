#Create a variable name and store your name in it. Print it.

name = "vansh"
print(name) #output:- vansh

#Store your age in a variable called age and print it.

age = 20
print(age) # output:- 20 the age store the age variable just beacous of the print of the variable the output


#Create two variables a and b. Print their sum.

number = 10
number2 = 20
print(number + number2) #output:- 30

#Store a city name in city and print a sentence using the variable.

city = "puna"
print(f"i love the {city}") #output:- i love the puna



#Store a number in price and print its datatype.

price = 555
print(price) #output:- 555
print(type(price))  #output:- intger



# Create one string variable and one integer variable and print both.

name = "vamnshh"
age = 22
print(name , age) #output:- name - vanshh and age - 22

print(type(name)) #output:- vanshh - string 
print(type(age)) #output:-  22 - intger


#Swap two variables without using a third variable.

a = 10
b = 20

a , b = b , a

print(a) #output:- 20
print(b) #output:- 10
print(type(a)) #output:- intger
print(type(b)) #output:- intger


#Create a variable marks and store a float value.
marks = 76.56

print(marks) #output:- 76.56
print(type(marks)) #output:- float


#Store a boolean value in a variable and print it.\

# try:
#     name = true
#     print(name) #output:- true
# except:
#     print("the name is not correct please boolean  value is check 1st or not")
    


#Store a boolean value in a variable and print it.\

name = True 
print(name) #output:- true 
print(type(name)) #output:- boolean 

name = False
print(name) #output:- False
print(type(name)) #output:- boolean


#Print datatype of both variables.

number = "22"
number2 = 22
number3 = 22.90
print(type(number)) #output:- string 
print(type(number2)) #output:- intger
print(type(number3)) #output:- boolean

'''
# BASIC TO MEDIUM LEVEL
'''

#Use variables length and width to calculate rectangle area.

length = 30
width = 50

rectangle_area = (length * width) #the formula of the area this formulas are use than the get your answer

print(rectangle_area) #output:- 1500


#Store marks of 3 subjects in variables and calculate average.

marks1 = 76
marks2 = 57
marks3 = 43

#Average = Total Marks / Number of Subjects

Average = (marks + marks + marks) / 3 #formula for average
# jitna bhi hai total usko divide karna padta hai uske marks ke sath 

print(Average) #output:- 76.56


# Store first name and last name separately and print full name.

# user  = input("enter your name :- ")
# user1  = input("enter your surname :- ")


# print(user + user1) #output:- vanshhpatel
# print(user + " " + user1) #output:- vanshh patel



#Store temperature in Celsius and convert it to Fahrenheit.

celsius = 25

fahrenheit = (celsius * 9/5) +32

print(fahrenheit) #output:- 77.0


#Create a variable salary and add 10% increment.

salary = 220
increment = 10

new_increment = salary + (salary * increment /100) 

print(new_increment) #output:- 242.0


##Create a variable salary and add 10% dicrement.

salary = 220
dicrement = 10

new_salary = salary - (salary * dicrement / 100) #formula the formula are. the both are same  you can use the both of than
# new_salary = salary * (100 - dicrement) /100  
print(new_salary)


#Store a number in num and print square and cube. 

number = 5

square = (number * number) #formula of square
print(square) #output:-  25

#Store a number in num and print cube. 
number1 = 5

cube  = (number1 * number1 * number1) #formula of cube

print(cube) #output:- 125


#Combine two string variables into one sentence.

name = "vansh"
age = 23

print(f'my name is {name} and i am {age} years old') 

#output:- my name is vansh and i am 23 years old


#Convert minutes into hours and remaining minutes.

total_minutes = 120

hours = total_minutes // 60
minutes = total_minutes % 60

print(hours)  #output:- 2. hours
print(minutes) #output:- 0. minute

minutes = 120

hours = minutes // 60
reaming = minutes % 60

print(f"hours {hours} and the {reaming} reaming") #output:- hours 2  0 reaming


#Combine two string variables into one sentence.

name1 = "my name is vianshh"
name2 = "and i from india"

print(name1 + " " + name2)

#------------------------------------

name1 = "vansh"
name2 = "23"

print(f"my name is {name1} i from india my age is {name2} years old")



#Calculate area of a circle using variable radius.

radius = 10

area = 3.14 * (radius * radius)

print(area) #output:- 314.0


'''
#  MEDIUM LEVEL
'''


#Store an amount and print final amount after GST.

amount  = 300
GST = 15

final_amount = amount + (amount * GST / 100)

print(final_amount) #output:- 345.0


#Calculate simple interest using variables.

money = 2000
interest_rate = 10
time_year = 1

final_intrest = (money * interest_rate * time_year /100) #the formula of the simple interest

print(final_intrest) #output:- 200.0 only simple interest rate in one years



#Store a 5-digit number and print its last digit.

number = "1 , 2 , 3 , 4 , 5"

print(number[-1]) #output:- negative indexing is -1 the answer the (5)


#Print first digit of a number stored in variable num.


number = 1 , 2 , 3 , 4 , 5

print(number[0]) #output:- 1

#NUMBER = 12345
#print(str(number) [0]) #convert the intger to string than answer the (1)



#Compare two variables and store result in another variable.

number1 = 10
number2 = 10

number = number1 == number2

print(number) #output:- true


#Store a string and save its length in another variable.

name  = "my name is vanshhh and i am 23 years old"

name1 = len(name)

print(name1) #output:- 40


#Store a name and convert it to uppercase.

name = 'my name is vanshh and  am from india'

name1 = name.upper() # inbuild function  in python

print(name1) # MY NAME IS VANSHH AND  AM FROM INDIA

name = "MY NAME IS VANSHH AND I AM FROM THE INDIA AND I 23 YERAS OLD "

name1 = name.lower()  # inbuild function  in python

print(name1) #my name is vanshh and i am from the india and i 23 yeras old 


#Store a sentence and count total words.

name = "my name is vanshh  and i am from the india and i 23 yeras old "

name1 = len(name.split()) #Python me words count karne ke liye .split() use hota hai.
print(name1)  #output:- 15


#Store division, floor division, and modulus in separate variables.

number = 11
division = number / 10
print(division)  #output:- 1.1

floor_division = number // 10
print(floor_division) #output:- 1

modulus = number % 10
print(modulus) #output:- 1






