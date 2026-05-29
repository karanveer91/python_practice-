"""
Calculate square root.
Store a random number in a variable.
Check palindrome using variables.
Check prime number.
Calculate factorial.
Generate Fibonacci sequence.
Calculate power of a number.
Perform modulus operation.

"""

#Calculate square root.
import math

num = 25
new_num = math.sqrt(num)
print(new_num)

'''
1:- Calculate Square Root

Code
import math

num = 25
result = math.sqrt(num)

print(result)
Baby Explanation 👶

Step 1
import math
Python ka math toolbox open kar rahe hain.

Step 2
num = 25

Ek variable num banaya
Usme number 25 store kiya

Step 3
result = math.sqrt(num)

sqrt = square root

Matlab

√25 = 5

To result me 5 store ho gaya

Step 4

print(result)

Output:

5.0
'''

#Store a random number in a variable.
import random
number = random.randint(1,20)
print(number)

'''
Store a Random Number
Code
import random

num = random.randint(1, 100)

print(num)
Explanation 👶

Step 1

import random

Python ko bol rahe hain
random number generate karo.

Step 2

random.randint(1,100)

Matlab
1 se 100 ke beech koi bhi number

Example output

57
Har baar different number aayega.
'''


#Check palindrome using variables.
num = "1212121"
reverse = num[::-1]
if num == reverse:
    print("palindrome")  #output:- palindrome
else:
    print("not palindrome")
    
#--------------------------------- 
num = "madam"
reverse = num[::-1]
if num == reverse:
    print("palindrome")  #output:- palindrome
else:
    print("not palindrome")

#---------------------------------     
num = "vanshh"
reverse = num[::-1]
if num == reverse:
    print("palindrome")
else:
    print("not palindrome")   #output:- not palindrome


'''
Palindrome = ulta aur seedha same

Explanation 👶
Step 1

num = "121"

number store kiya.

Step 2

rev = num[::-1]

[::-1] matlab reverse

121 → 121

Step 3

if num == rev

check kar rahe hain

121 == 121

True

Output

Palindrome
'''

#Check prime number.

num = int(input("check the number prime or not:-"))
for x in range(2, num):
    if num % x == 0:
        print("not a prime number")
        break
else:
    print("prime number")

"""
Prime Number kya hota hai?

Prime Number wo number hota hai jo sirf 2 numbers se divide hota ho:

1:- 1 se
2:- khud se
Aur kisi se nahi.
------------------------------------------------
Example 5

5 ÷ 1 = 5
5 ÷ 5 = 1

Sirf 2 divisions → Prime

Example 7

7 % 1 = 7
7 % 2 = 1
7 % 3 = 1
answer:- prime number

Example 11

11 % 1 = 11  #only ye do number check honge agr 0 nahi aaya toye prime number hai 
11 % 2 = 1   #only ye do number check honge agr 0 nahi aaya toye prime number hai 
11 % 3 = 0
answer:- prime number


--------------------------------------------------

❌ Not Prime

Example 6

6 ÷ 1 = 6
6 ÷ 2 = 0
6 ÷ 3 = 0
answer:- not a prime number

Ye 4 numbers se divide ho gaya hai is liye prime number nahi hai

Example 9

9 % 1 = 9
9 % 2 = 1
9 % 3 = 0  #jaha pe 0 mila ohh not a prime number hai

answer:- not a prime number

"""  

#claculate the factorial
num = 5
fact = 1
for i in range(1,num+1):
    fact = fact * i
    print(fact)  #output:- 120

"""
Factorial kya hota hai?

Factorial ka matlab hai:

👉 Kisi number ko uske niche wale sab numbers se multiply karna.

-------------------------------------------------------------------------
Baby Step Explanation
Step 1
num = 5

Factorial nikalna hai 5 ka

Step 2
fact = 1

Result store karne ke liye variable.

Step 3

Loop chalega

range(1,6)

Values

1 2 3 4 5
Step 4 Calculation

------------------------------------------------

Start

fact = 1

Iteration 1

1 * 1 = 1

Iteration 2

1 * 2 = 2

Iteration 3

2 * 3 = 6

Iteration 4

6 * 4 = 24

Iteration 5

24 * 5 = 120

✅ Final Output
120
"""

#Calculate power of a number.
a = 2
b = 3
result = a ** b
print(result)    #output:- 8

"""
Explanation 👶
** = power operator

Calculation

2 ** 3 = 8

Output :- 8

"""

#Perform modulus operation.
num = int(input("enter your name:-"))
if num % 2 == 0:
    print("even") #agr 
else:
    print("odd") #agr 
















