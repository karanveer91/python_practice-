'''
Calculate percentage.
Calculate grade.
Calculate profit and loss.
Calculate distance.
Calculate speed.
Calculate time.
Area of rectangle.
Area of circle.
Perimeter of square.
Perimeter of rectangle.
Perimeter of triangle.
Count odd and even digits.

'''

#Calculate percentage.
student_Marks = 436
total = 500
total_marks = (student_Marks / total) * 100

print(total_marks) #output:- 87.2


#Calculate grade.
Marks = int(input("enter your marks:- "))
if Marks >= 90 and Marks <= 100:
    print("A+")
elif Marks >= 70 and Marks <= 89:
    print("B+")
elif Marks >= 50 and Marks <= 69:
    print("C")
elif Marks >= 35 and Marks <= 49:
    print("D")
else:
    print("Fail")


# Calculate profit and loss.
Profit = 130
selling_price = 120
if Profit > selling_price:
    print("profit", Profit - selling_price) #output:-  profit 10
else:
    print("loss", selling_price - Profit)


#Calculate distance.

speed = 15 #bike speed 15
time = 2  #2 hours
distance = (speed * time)
print(distance) # output:- 30km

#Calculate speed.
distance = 30
time = 2 # 2 hour
speed = (distance / time)
print(speed) #output:- 15km in 


#Calculate time.
distance = 120
speed = 50
time = (distance / speed)
print("hours", time)   #output:-  hours 2.4


#Area of rectangle.
length = 10
width = 5

area = (length * width)
print(area)


#Perimeter of square.
side = 5
parameter = 4 * side
print(parameter) #output:-  20





#Perimeter of triangle.
a = 2
b = 4 
c = 3
parameter = a + b + c 
print(parameter)


#Count odd and even digits.
num = 123456

even = 0
odd = 0
for x in str(num):
    if int(x) % 2 == 0:
        even += 1
    else:
        odd += 1
print('odd',odd)
print('even',even)

"""
Number Store Karna
num = 123456

Yaha ek variable num banaya.

Usme number store kiya:

123456
2 Counters Banana
even = 0
odd = 0

Ye counting boxes hain 📦

Variable	Meaning
even	even digits count
odd	odd digits count

Start me dono 0 hain.

3 Number ko String me Convert Karna
for digit in str(num):

Important part.

str(num) ka matlab:

123456 → "123456"

Ab Python number ko characters me tod sakta hai.

Loop me digits milenge:

1
2
3
4
5
6

4 Loop Start
Iteration 1

digit = 1

Check:

1 % 2 = 1

Odd number

odd = 1
Iteration 2

digit = 2

2 % 2 = 0

Even number

even = 1
Iteration 3

digit = 3

3 % 2 = 1

Odd

odd = 2
Iteration 4

digit = 4

4 % 2 = 0

Even

even = 2
Iteration 5

digit = 5

5 % 2 = 1

Odd

odd = 3
Iteration 6

digit = 6

6 % 2 = 0

Even

even = 3

5 Final Output
print("Even digits:", even)
print("Odd digits:", odd)

Output

Even digits: 3
Odd digits: 3
"""

