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

















