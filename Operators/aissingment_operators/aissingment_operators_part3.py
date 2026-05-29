'''
## SECTION 1: ASSIGNMENT OPERATORS
( = += -= *= /= //= %= **= )
30 Questions

21. Take a number and decrement it by 1 using -=.
22. Create x = 100. Apply //= 3. Print result.
23. Take a float number and apply *= 2.5.
24. Create x = 81. Apply **= 0.5 (square root).
25. Take a number and update it three times using +=.
26. Create amount = 10000. Increase by 5% using *=.
27. Create x = 15. Apply %= 4 and then += 2.
28. Take a number and apply /= 3, then *= 2.
29. Create x = 7. Apply **= 2 and then -= 10.
30. Take a number and apply a chain of operations using assignment operators.
'''

#21. Take a number and decrement it by 1 using -=.
number = int(input('enter your number :- '))

# new_number = number - 1
number -= 1
print(number)

'''
enter your number :- 23
22
'''

#22. Create x = 100. Apply //= 3. Print result.
create = 100

# new_create = create // 3
create //= 3
print(create) #output:-  33

'''
Ab calculation karte hain
100 ÷ 3

Normal division:

100 ÷ 3 = 33.3333

Lekin // floor division hota hai.

Matlab:

decimal hata do

To result:

33
4 Final value
x = 33

5 Print
print(x)

Output:

33
'''

#24. Create x = 81. Apply **= 0.5 (square root).

create = 81 

# new_create = create ** 0.5
create **= 0.5
print(create)  #output:- 9.0


#25. Take a number and update it three times using +=.
#Take a number and update it three times using +=.
number = int(input("enter your number :- "))

number += 1
number += 2 
number += 3 

print(number)

'''
enter your number :- 1
7
'''


#26. Create x = 15. Apply %= 4 and then += 2.

create = 15 

new_create = create % 4 + 2
print(new_create) #output :- 5

create %= 4 
create += 2 
print(create) #output :- 5


#27 take a number and apply /= 3, then *= 2.

number = int(input("enter your number :- "))

new_number = number / 3 * 2
print(new_number) #output:- 8.0 

number /= 3
number *= 2
print(number) #output:- 8.0


'''
Method 1 (single line)
new_number = 12 / 3 * 2
Step 1
12 / 3 = 4
Step 2
4 * 2 = 8

Output:

8.0

'''


#29 Create x = 7. Apply **= 2 and then -= 10.

create = 7
new_create = create ** 2 - 10
print(new_create) #output:- 39

create **= 2
create -= 10
print(create) #output;- 39

'''
Step-by-Step
1️⃣ Step
create = 7
2️⃣ Step (Power)
create **= 2

Matlab:

create = create ** 2

Calculation:

7 × 7 = 49

Ab:

create = 49
3️⃣ Step (Subtract)
create -= 10

Matlab:

create = create - 10

Calculation:

49 - 10 = 39
📌 Final Output
39



'''

#30 take a number and apply a chain of operations using assignment operators.

number = int(input('enter your number :- '))

number += 5
number -= 5
number /= 5
number //= 5
number *= 5
number **= 5
number %= 5

print(number)

'''
🔎 Example lete hain

Maan lo input:

enter your number :- 10
🧠 Step-by-Step Breakdown
1️⃣ Start
number = 10
2️⃣ += 5
10 + 5 = 15
3️⃣ -= 5
15 - 5 = 10

👉 Yaha tum wapas same number par aa gaye 😄

4️⃣ /= 5
10 / 5 = 2.0
5️⃣ //= 5
2.0 // 5 = 0.0

👉 Important step ⚠️
2 ko 5 se divide → 0.4
Floor → 0.0

6️⃣ *= 5
0.0 × 5 = 0.0
7️⃣ **= 5
0.0 ^ 5 = 0.0
8️⃣ %= 5
0.0 % 5 = 0.0
📌 Final Output

0.0

'''

