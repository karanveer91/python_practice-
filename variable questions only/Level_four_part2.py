#Count digits in a number.
number = [1 , 2, 3, 4, 90, 10, 20]
for x in range(9):
 print((number), x)
 
 #how to find length.
number = "PYTHON"
print(len(number))  #output:- 6 kisi ki length check karana hai to hum length function ka use karte hai

#Reverse a number.
number = [1,2,3,4,5,6,7,8,9]
#index   0,1,2,3,4,5,6,7,8  #positive index
#reverse 9,8,7,6,5,4,3,2,1  #negative index
print(len(number))  #output:- 9
print(number[1:6:2])  #output:- (2, 4, 6)
print(number[-1::-1])   #reverse output:- (9, 8, 7, 6, 5, 4, 3, 2, 1)
'''
[start : stop : step]
[  1   :  9   :  1  ]

------------------------------

print(number[ -1 :   :  -1 ]) #output:- same reverse ho jayega  :- (9, 8, 7, 6, 5, 4, 3, 2, 1)
print(number[    :   :  -1 ]) #output:- same reverse ho jayega  :- (9, 8, 7, 6, 5, 4, 3, 2, 1)

start = -1  → last element
step = -1   → reverse direction

'''


#Find last digit of a number.
number = [1,2,3,4,5,6,7]
print(len(number))  #total len output:- 7
print(number[-1::]) #output:-  find last digit number:- 7
#--------------------------------------
number = 123456
print(number % 10)  #output:- find last digit number:- 6

'''
“Find last digit of a number.

Example:
number = 4567
Last digit nikalne ka formula:
number % 10

Python code:
number = 4567
print(number % 10)

Output:- 7

'''


#Find first digit of a number.
number = [1,2,3,4,5,6,7]
print(number[0])

'''
agr muje index bhi print krna hai to kaise karu.

Method 1 — range() use karke
number = [1,2,3,4,5,6,7]

for i in range(len(number)):
    print("Index:", i, "Value:", number[i])

  
Output
Index: 0 Value: 1
Index: 1 Value: 2
Index: 2 Value: 3
Index: 3 Value: 4
Index: 4 Value: 5
Index: 5 Value: 6
Index: 6 Value: 7

Explanation:

range(len(number))

Matlab 0 se last index tak loop chalega.

'''

#modulus operation.
num1 = 10
num2 = 3
remanider = num1 % num2
print(remanider)




