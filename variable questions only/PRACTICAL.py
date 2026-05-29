#Create three variables: age (int), salary (float), name (str). Print all three.
name = 'vanshh patil'
age = 22
salary = 3.5
print(f"my name is {name} is and I’m {age} years old and my {salary} LPA")
print(f'my name is {name} is and I’m {age} years old and my {salary} LPA')

"""
Output
my name is vanshh patil is and I’m 22 years old and my 3.5 LPA |
my name is vanshh patil is and I’m 22 years old and my 3.5 LPA |

"""

#Take a string "50", convert it to integer, and add 20 to it.
convert = int("50")
print(convert + 20)

# Output :- 70 

#Create two float numbers and print their division result.
a = 3453.076
b = 45526.90

print(a / b)
print(a // b)
print(a * b)
    
"""
Output
0.07584693884275011
0.0
157207845.7444
"""
#Create a variable x = 25. Convert it into float and print its type.
x = float(25.)
y = int(25.)
z = str(25.)

print(type(x))
print(type(y))
print(type(z))

"""
Output
<class 'float'>
<class 'int'>
<class 'str'>
"""

#Create a variable price = 99.99. Convert it into int. Print result and explain what happened.
price = int(245.99)
print(price)

# Output :- 245

#Create a variable name = "Python". Print the first character.
name = 'PYTHON'
print(name[0])      # P
print(name[0:1:1])  # P
print(name[0:2:1])  # PY
print(name[1:4:1])  # YTH
print(name[0::2])   # PTO

#Create a string "100". Convert it to float, then multiply it by 2.
name = float("100")
convert = float("200")

print(name*2)     #200.0
print(convert*2)  #400.0

"""
8. Create two variables:
    
    a = "Hello"
    
    b = "World"
    
    Print: Hello World
"""
A = "Hello"
B = "World"

print(A, "" + B) # Hello World
print(A + B)     # HelloWorld


"""
9. Create a variable x = 5. Print:
    
    The value of x is 5
    
    (Use type conversion properly.)
"""
X = 5
print(f'The value of x is {X}')

# Output :- The value of x is 5


"""
10. Create three variables:
    
    length = 5
    
    width = 2.5
    
    Compute area and print result. Also print its data type.
"""

Lenght = 5 
Width = 2.5
Area = (Lenght * Width)
print(Area)  #12.5

A = 3
B = 3.5
print(type(A *B),A * B)   # 10.0






