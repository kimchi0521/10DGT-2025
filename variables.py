# Demonstrate how variables work in python

# Author: JJ Lee
# Date: 8-10-2025
# version 1.1

# Different types of variables
# Store a string
greeting = "hello world"
print(greeting)

# Store a number
my_number = 75 # Assigned the number 75 to the variable "my_number"
print(my_number)

my_number2 = 9
print(my_number2)

# Assigning the value of one variable to another
my_number = greeting
print(my_number) # Don't assign values to variables that don't make sense for its name

''' This lets
me press enter as many times
as I want and keeps
it as a comment. Useful for
long comments.'''

#Creating new variables
num_1 = 8
num_2 = 15

sum1 = 8 + 15 # This is not goot practice
print(sum1)

sum1 = num_1 + num_2
print(sum1)

sum_string1 = "8"
sum_string2 = "15"

# Adding two strings together. This is called a concatenation
sum = sum_string1 + sum_string2
print(sum)

# Print formatting. f stands for format and insert the names of variables into the curly brackets
print(f"My calculation for {num_1} and {num_2} is {sum1}")
