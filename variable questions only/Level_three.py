"""
LEVEL 3 — Thinking Level:-

Convert an integer to a string.
Convert "100" to integer.
Convert float to integer.
Convert integer to float.
Convert "25" to float.
Convert "3.14" to float.
Add "50" and 20 after conversion.
Print result and type of 10 + 5.5.
Check result of True + 5.
Check result of False + 10.
Swap two variables using a third variable.
Swap two variables without using a third variable.
Check if num = 7 is even or odd.
Calculate area of circle using radius.
Calculate area of square using side.
Calculate area of triangle using base and height.
Convert seconds = 3600 to hours.
Convert minutes = 120 to hours.
Convert km = 5 to meters.
Convert kg = 2 to grams.
Apply 10% discount on price = 500.
Convert marks = 75 into percentage.
Find square of a number.
Find cube of a number.
Check if a year is a leap year using a variable.
"""


#Convert an integer to a string.
number = 20
number = str(number)
print(number)       #output:- 20
print(type(number)) #output:- string

#Convert "100" to integer.
number = "100"
number = int(number)
print(number)       #output:- 100
print(type(number)) #output:- integer

#Convert float to integer.
number = 22.5
number = int(number)
print(number)       #output:- 22
print(type(number)) #output:- integer

#Convert integer to float.
number = 20
number = float(number)
print(number)       #output:- 20.0
print(type(number)) #output:- float


#Convert "25" to float.
number = "25"
number = float(number)
print(number)       #output:- 25.0
print(type(number)) #output:- float

#Add "50" and 20 after conversion.
add = int("50")
add = (add - 30)
print(add)  #output:- 20

#Add "50" and 20 and print.
add2 = int(50)
add2 = (add2 + 20)
print(add2)  #output:- 70

#Print result and type of 10 + 5.5.
a = 10
a = (a + 5.5)
print(a) #output:- 15.5
print(type(a)) #output:- float


#Check result of True + 5.
num = True
num = (True + 5)
print(num)  #output:- 6
print(type(num))  #output:- integer

#Check result of False + 5.
num = False
num = (False + 5)
print(num)  #output:- 5
print(type(num))  #output:- integer 


#Swap two variables using a third variable.
a = 10
b = 20
a, b = b, a
print("a =", a) #output:- a = 20
print("b =", b) #output:- b = 10

# c = (b,a) #output:- (b 10, a 20)
# print(c) #output:- (20,10)

#Check if num = 7 is even or odd.
num = 23
if num % 2:
    print("ODD") #agr number bach raha hai like 23 me. 1. bach raha hai is liye ohh ek (ODD) number hai

else:
    print("EVEN") #agr number nahi bach raha hai like samj lo 24 hai isme koi number nahi bach raha hai 0 bach raha hai ohh ek (EVEN) number hai
    
"""
 print("ODD") #agr number bach raha hai like 23 me. 1. bach raha hai is liye ohh ek (ODD) number hai
 
  print("EVEN") #agr number nahi bach raha hai like samj lo 24 hai isme koi number nahi bach raha hai 0 bach raha hai
  ohh ek (EVEN) number hai
"""

#calculate area of circle using radius.
calculate = 20
calculate = (3.14 * calculate * calculate)  #Agar radius 10 hai  (13.14 * 10*10) , Agar radius 20 hai  (13.14 * 20*20)
print(calculate)  #output:- 1256.0   20 ka output hai


#Convert marks = 75 into percentage.
Marks = float(75)
print(f"my persentage is {Marks}%") #output:- my persentage is 75.0%


Marks = 75.322
total = 100
persentage = (Marks / total) * 100
print(f"my persentage is {persentage}%") #output:- my persentage is 75.0%
print(f"my persentage is {persentage:.2f}%")  #output:- my persentage is 75.32%

"""
Agar sirf 2 decimal tak hi dikhana ho (best practice)

percentage = 71.93456
print(f"My percentage is {percentage:.2f}%")

"""

#Apply 10% discount on price = 500.
price = 500
new_price = price - (price * 10 / 100)
print(new_price)    #output:- 450.0

price = 200
discount = 10

new_price = price - (price * discount / 100) 
print(new_price)  #output:- 180.0



#Find square of a number.

square = 5
new_square = (square ** 2)
print(new_square) #output:- 25

#Find cube of a number.

cube = 5
new_cube = (cube ** 3)
print(new_cube) #output:- 125






