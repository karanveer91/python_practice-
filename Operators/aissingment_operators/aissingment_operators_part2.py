'''
## SECTION 1: ASSIGNMENT OPERATORS
( = += -= *= /= //= %= **= )
30 Questions

11. Take two numbers a and b. Add b into a using +=.
12. Take price = 1000. Apply 10% discount using -=.
13. Create count = 0. Increase it 5 times using += inside code.
14. Create total = 100. Multiply by 1.5 using *=.
15. Take a number and reduce it by half using /= 2.
16. Create x = 50. Apply -= 20 and print result.
17. Take number from input and apply %= 2. Print result.
18. Create value = 3. Apply **= 4. Print result.
19. Create balance = 2000. Add 500, subtract 300 using assignment operators.
20. Take a number and increment it by 1 using +=.
'''


#11. Take two numbers a and b. Add b into a using +=

number1 = int(input("enter your your 1st number :- "))
number2 = int(input("enter your your 2nd number :- "))

number1 += number2
print(number1)

'''
enter your your 1st number :- 200 
enter your your 2nd number :- 2
202
'''

#12. Take price = 1000. Apply 10% discount using -=.

price = int(input("enter your price :- "))
discount = 10
final_discount = price * discount / 100
price -= final_discount

print(price)

'''
enter your price :- 200
180.0
'''

#13. Create count = 0. Increase it 5 times using += inside code.

count = 0
for i in range(5):
    count += 1
    print(count)
        
'''
output:-
1
2
3
4
5
'''

#14. Create total = 100. Multiply by 1.5 using *=.
create_total = 100
create_total *= 1.5

print(create_total)  #output:- 150.0

#---------------------------------------------------------

#14. Create total = 100. Multiply by 1.5 using *=.
create_total = 100
total = create_total * 1.5

print(total)  #output:- 150.0


#15. Take a number and reduce it by half using /= 2.
number = int(input("enter your number :- "))

total = number / 2
print(total)

'''
enter your number :- 200 
100.0
'''
#--------------------------------------------------

number = int(input("enter your number :- "))
number /= 2
print(number)

'''
enter your number :- 1000
500.0
'''

#16. Create x = 50. Apply -= 20 and print result.
create = 50
create -= 20
print(create) #output:- 30

create = 50 
new_create = create - 20
print(new_create) #output:- 30


#17. Take number from input and apply %= 2. Print result.
number = int(input("enter your number :- "))
new_number = number % 2
# number %= 2
print(number)

#18. Create value = 3. Apply **= 4. Print result.
create = 3
create **= 4
# new_create = create ** 4
print(create)

'''
Calculation
value = 3 ** 4

Matlab:

3 * 3 * 3 * 3

Step by step:

3 * 3 = 9
9 * 3 = 27
27 * 3 = 81
4️⃣ Final Output
print(value)

Output:

81
-----------------------------------------
📌 Power ka meaning
3 ** 4

Matlab:

3 ko 4 baar multiply karo

Isliye:

3 * 3 * 3 * 3
🔎 Step-by-Step Multiplication
Step 1
3 * 3 = 9

Ab result 9 ho gaya.

Step 2
9 * 3 = 27

Ab result 27 ho gaya.

Step 3
27 * 3 = 81

Final result 81.
'''


#19. Create balance = 2000. Add 500, subtract 300 using assignment operators.
balance = 2000
new_balance = balance + 500 - 300
print(new_balance) #output:- 2200



#20 take a number and increment it by 1 using +=.
number = int(input("enter your numbeer :- "))
number += 1
print(number)

'''
enter your numbeer :- 5
6
'''

