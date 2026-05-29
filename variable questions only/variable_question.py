"""
Basic Variable Questions:-

Ek variable name banaye aur usme apna naam store kare. Usko print kare.
Ek variable age banaye aur usme apni age store kare. Usko print kare.
Ek variable city banaye aur usme apne city ka naam store kare.
Ek variable salary banaye aur usme float value store kare (example: 50000.50).
Teen variables name, age, city bana kar ek sentence print kare.

"""
#Ek variable name banaye aur usme apna naam store kare. Usko print kare.
name = "vansh"
print(name) # output :- vansh

#Ek variable age banaye aur usme apni age store kare. Usko print kare.
name = "vansh"
age = 23
print(f'my name is {name} and I’m {age} year old')


#output:- my name is vansh and I’m 23 year old

#Ek variable city banaye aur usme apne city ka naam store kare.
name = "vansh"
age = 23
city = "puna"
print(f"my name is. {name} and I’m {age} year old my city is {city}")

#output :- my name is vash and I’m 23. years old my city is puna

#Ek variable salary banaye aur usme float value store kare (example: 50000.50).
salary = 50000.550
print(salary)   # 50000.55

#Teen variables name, age, city bana kar ek sentence print kare.
name = "sam"
age = 23
city = "puna"
print(name, age, city)
print(f"my name is {name} I’m {age} years old and my city name is {city}")

#output:- sam 23 puna
#2nd output:- my name is sam I’m 23 years old and my city name is puna


"""
Data Type Identification

Ek variable a = 10 banaye aur uska data type print kare.
Ek variable b = 5.5 banaye aur uska data type print kare.
Ek variable c = "Python" banaye aur uska data type print kare.
Ek variable d = True banaye aur uska data type print kare.
Ek variable e = None banaye aur uska data type print kare.
"""

#Ek variable a = 10 banaye aur uska data type print kare.
A = 10
print(type(A))
#output:- INT DATA TYPE

#Ek variable b = 5.5 banaye aur uska data type print kare.
B = 5.5 
print(type(B))
#output:- float data type


#Ek variable c = "Python" banaye aur uska data type print kare.
C = "PYTHON"
print(type(C))

#output:-  string data type

#Ek variable d = True banaye aur uska data type print kare.
d = True
e = False
print(type(d))
print(type(e))

#output:- bool
#output:- bool


#Ek variable e = None banaye aur uska data type print kare.
F = None
print(type(F))

#output:- nonetype

"""
Multiple Variables

Ek hi line me x, y, z variables ko 10, 20, 30 assign kare.
Ek hi value 100 ko a, b, c teen variables me store kare.
name, age, salary variables bana kar ek formatted sentence print kare.

"""

#Ek hi line me x, y, z variables ko 10, 20, 30 assign kare.
A,B,C = 10 , 20, 30
print(A,B,C)

#Output:- 10 20 30


#Ek hi value 100 ko a, b, c teen variables me store kare.
A = 100
B = A
C = B
print(A,B,C)

#Output:- 100 100 100



#name, age, salary variables bana kar ek formatted sentence print kare.
name = "vansh"
age = 23
city = "puna"
print(f"my name is {name} I’m {age} years old my city name is {city}")

#OUTPUT:- my name is vansh I’m 23 years old my city name is puna


"""
Type Conversion

Ek integer 10 ko string me convert kare.
Ek string "50" ko integer me convert kare.
Ek integer 25 ko float me convert kare.
Ek float 9.8 ko integer me convert kare.

"""

#Ek integer 10 ko string me convert kare.
number = str(10)

print(number)
print(type(number))

#output:- 10
#output:- str


#Ek string "50" ko integer me convert kare.
name = int(50)
print(name)
print(type(name))

#output:- 50
#output:- integer

#Ek integer 25 ko float me convert kare.
name = float(25)
print(name)
print(type(name))

#output:- 25.0
#output:- float

#Ek float 9.8 ko integer me convert kare.
name = int(9.8)
print(name)
print(type(name))

#output:- 9
#output:- integer

"""
Small Practice Problems

Do variables num1 aur num2 bana kar unka sum print kare.
Ek variable price aur quantity bana kar total cost calculate kare.
Ek variable pi = 3.14 bana kar uska data type print kare.
Ek variable is_student = True bana kar print kare.
first_name aur last_name variables bana kar full name print kare.

"""

#Do variables num1 aur num2 bana kar unka sum print kare.
num1 = 10
num2 = 20
print(num1 + num2) #30

num3 = 20
num4 = 20
print(num3 + num4) #40


#Ek variable price aur quantity bana kar total cost calculate kare.
price = 350
quantity = 2
print(price * quantity) # 700


#Ek variable pi = 3.14 bana kar uska data type print kare.
pi = 13.14
print(pi)       #output:- 13.14
print(type(pi)) #output:- float


#Ek variable is_student = True bana kar print kare.
is_student = True
print(not is_student)  #output:- false
print(is_student)      #output:- true


#first_name aur last_name variables bana kar full name print kare.
name = "sandip"
middle_name = "dnyaneshawar"
suer_name = "patil"

print(name + middle_name + suer_name)   #output:- sandipdnyaneshawarpatil
print(name + " ", middle_name + " " , suer_name)   #output:- sandip  dnyaneshawar  patil



"""
Little Thinking Questions

x = 5, y = "5" — dono ka data type print kare.
a = 10, b = 3.5 — a * b ka result aur type print kare.
Ek variable temperature = 37.5 bana kar uska type check kare.

"""

#x = 5, y = "5" — dono ka data type print kare.
x = 5
y = "5"
z = 5.55
print(type(x))  #output:- integer
print(type(y))  #output:- string
print(type(z))  #output:- float


#a = 10, b = 3.5 — a * b ka result aur type print kare.
a = 10
b = 3.5
c = a * b
print(c)         #output:- 35.0
print(type(c))   #output:- float



#Ek variable temperature = 37.5 bana kar uska type check kare.

temperature = 37.5
print(temperature)       #output:- 37.5
print(type(temperature))  #output:- float

















