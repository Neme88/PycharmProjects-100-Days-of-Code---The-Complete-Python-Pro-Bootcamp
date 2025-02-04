# Write your code below this line 👇
# Day 1 print function, strings, string concatenation, creating newline, input function,
# len function Variables and final project(band name generator).
print("Hello world!")
# string manipulation series
# we will print five lines of code using one print statement and \n to create new lines
print("first line\nsecond line\nthird line\nfourth line\nfifth line\n")
# first way to insert space between strings is concatenation
print("Hello" " " + "world")
# or
print( "Hello" + " " + "world" )
# second way to insert space between strings without the plus
print("Hello " "world")
# line 15 below we demonstrated putting function to another function by putting the input function side the print function
# print("Hello " + input("What is your name?") + "!")
# implementing the input function in a more readable format
# User_name = input("What is your name: \n")
# print("Hello " + User_name + "!")
# in this course we also treated commenting in python using # sign
#  Also the crl / to comment and uncomment a line of code.

# In this course session we will be learning python Variables
# Variable implementation in python
# implementing variable on a string datatype
name = "Jack"
print(name)
# implementing variable on number data type
phone_number = 234567890
print(phone_number)
# implementing variable on a boolean datatype
isSunShine = True
print(isSunShine)
# implementing variable on a function
#input_name = input("Enter your name: \n")
# print(input_name)
# course exercise
# first course session exercise finding the length of an inputted string in a oneline solution
#print(len(input("what is your name:\n ")))
# second course solution finding the length of an inputted string in multiple line solution
# username = input("what is your name?\n")
# length = len(username)
# print(length)

# In this course session we learnt what is variable and variable implementation on different datatypes in python we did exercise
#  on getting the length of inputted the string in one line and a second exericse on the same function but this time in multiple lines
# Final project starts here
# print("Welcome to the Band Generator.")
# user_City_Name= input("What's the name of the city you grow up in?\n")
# user_Pet_Name = input("what's your pet's name?\n")
# print("your band name could be: " + user_City_Name + " " + user_Pet_Name )

# Day 2 Data types, Numbers, Operations, Type Conversion, f-Strings file day project(Tip Calculator)
# Data Type
# subscripting means pulling out individuel string
positive_number_subscripting = "Hello"
print(positive_number_subscripting[4])
# we can also achieve subscripting using negative numbers
negative_number_subscripting = positive_number_subscripting
print(negative_number_subscripting[-1])

# integer (whole numbers be it positive or negative) numbers without a decimal point
number = 56
print(123 + 345)
# Large integer
# in python we use underscore to present coma when separating the large number python does ignore the underscore the only benefit is for human visualization
print(123_456_789)
# float = floating point number( A number with decimal point.)
PI = 3.14159
print(PI)
# Boolean (true or false values)
is_Hot = False
print(is_Hot)
not_Hot = True
print(not_Hot)
# debug exercise caused by inputting integers in a len function
length_input = len("12345")
print(length_input)
# I chose to solve this problem by converting the integers to a string and print the as len function doesn't accept integers
# how to check any data type in python
# Datatype implementation quick exercise
print(type("Hello"))
print(type(100))
print(type(3.14))
print(type(False))

# type casting or type convertion means converting one datatype to another datatype
# implementation of type casting
print(int("156") + int("456"))
# the above code does addtion not concatenation because the strings are converted to int
# where it makes sense we can convert all four python datatypes to another datatype
# Error debug exercise
# below is the code with bug.
# print("Number of letters in your name: " + len(input("Enter your name")))
# debugged solution
# user_name = input("Enter your name ")
# length_of_user_name = len(user_name)
# print("Number of letters in your name: " + str(length_of_user_name))
# Mathematical operations in python
# Implementing PAMDASLR in python
"""
Parenthesis = ()
Exponent = ** 
Multiplication = * 
Division = / for floating point division and // for floor division 
Addition = +
Subtraction = -
"""
# code example
sum_of_expression = 10 * 10 + ( 6 - 2) + 2 / 3
print(sum_of_expression)
exponent = 3 ** 3
print(exponent)
multiplication = 3 * 3
print(multiplication)
floor_division = 6 // 2
print(floor_division)
floating_point_division = 7 / 3
addition = 3 + 2
print(addition)
subtraction = 5 - 3
print(subtraction)

# quick PEMDASLR exercise build a BMI calculator
"""
height = float(input("Enter your height in centimeter:\n"))
weight = int(input("Enter your weight in Kg:\n"))
bmi = weight / height ** 2
# achieved flooring to the nearst whole number using the int function to wrap our floating point result
print("Your bmi is:", int(bmi))
# We can achevie a more the accurate result using the round function which will either round up or down to the nearest who number depending
# on how near the decimal place numbers are to the nearest whole number this approach is advised way of achieving a cleaner output as round function is a mathematical operation in python
print("your bmi is :", round(bmi))
# implementing round function to an accurate result in such a way it gives us a floating point result with two decimal place instead
# The original result with a long decimal place.
print(f"your bmi is: {round(bmi, 2)}")
"""
# maths friendly functions and operators in python
#  round()
# assignment operators shorthand these short hands come handy when you are manipulation a value based on it previous value.
# +=
# -=
# *=
# /=

# f-string is a technique that helps us to insert different datatypes into a string while printing without having to go through the painful process of
# concatenating different values and having to convert theme before we can print. it is a very handy tool.
# example
# age = 10
# name = "Neme"
# isTall = True
# # f-string methed to print this values
# print(f"Your name is {name}, you are {age}years old, you are tall true or false ? {isTall}.")
# # final day project (build a tip calculator)
# implementation 1
# print("Welcome to tip calculator!")
# bill_amount =float(input("What was the total bill? $ \n"))
# tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
# people = int(input("How many people to split the bill? \n"))
# total_bill = (tip_amount / 100) * 100 + bill_amount # which is 10/100 = 0.1 * 100 = 10 + 100 which is 110
# bill_per_person = total_bill / people
# each_person_total = round(bill_per_person, 2)
# print(f"Each person should pay ${each_person_total}")
# # Implementation two
# print("Welcome to tip calculator!")
# bill_amount = float(input("What is the total bill? $"))
# tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# tip_percentage = tip_amount / 100
# total_bill = bill_amount + tip_percentage
# bill_per_person = total_bill / people
# final_bill = round(total_bill, 2 )
# print(f"Each person should pay {final_bill}")
# implementing the even or odd number check depend on what number user inputted
# if/else condtional statement

# user_input = int(input("Enter the number to be checked "))
# if/else conditional statement
# if user_input % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Nested if/else statement.
# print("Welcome to the rollercoaster!")
# height = int(input("Enter your height in cm: "))
# if height >= 120:
#     print("you can ride the rollercoaster ")
#     age = int(input("Enter age: "))
#     if age <= 12:
#         print("Pay $5")
#     elif age <= 18:
#         print("Pay $7")
#     else:
#         print("Pay $12")
# else:
#     print("Sorry you are not tall enough to ride.")

# exercise to build bmi calculator and incorporate if/elif/else conditional statement to interperprate the bmi values calculated
# height = 1.85
# weight = 83
# bmi = weight / (height ** 2)
# if bmi >= 25:
#     print("overweight")
# elif bmi >= 18:
#     print("normal weight")
# else:
#     print("underweght")


# Nested if/else statement.
# Multiple if statements
#  enhancing this code to include multiple if statements
# print("Welcome to the rollercoaster!")
# height = int(input("Enter your height in cm: "))
# bill = 0
# if height >= 120:
#     print("you can ride the rollercoaster ")
#     age = int(input("Enter age: "))
#     if age <= 12:
#         bill = 5
#         print("Children Pay $5")
#     elif age <= 18:
#         bill = 7
#         print("Teenagers Pay $7")
#     else:
#         bill = 12
#         print("Adults Pay $12")
#     wants_photos = input("do you want photos? type y for Yes and n for No.")
#     if wants_photos == 'y':
#         bill+= 3
#     print(f"Your filnal bill is ${bill}")
#
# else:
#     print("Sorry you are not tall enough to ride.")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pizza_price = 0
ordering_pizza = True

if ordering_pizza == True:
    if size == 'S':
        pizza_price = small_pizza_price
        print(f"Your final bill is: {pizza_price}.")
    elif size == 'M':
        pizza_price = medium_pizza_price
        print(f"Your final bill is: {pizza_price}.")
    elif size == 'L':
        pizza_price = large_pizza_price
        print(f"Your final bill is: {pizza_price}.")
    else:
        print("Enter valid pizza size")
    if pepperoni == 'Y' and size == 'S':
        pizza_price += 2
        print(f"Your final bill is: {pizza_price}.")
    if extra_cheese == 'Y' and size == 's' and pepperoni == 'Y':
        pizza_price += 3
        print(f"Your final bill is: {pizza_price}.")
    if pepperoni == 'Y' and size == 'M' or size == 'L':
        pizza_price += 3
        print(f"Your final bill is: {pizza_price}.")
    if extra_cheese == 'Y' and size == 'M' or size == 'L':
        pizza_price += 4
        print(f"Your final bill is: {pizza_price}.")

else:
    print("Do you want to order a pizza")






































