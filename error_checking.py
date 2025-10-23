# Error checking
# Author: JJ Lee
# Date: 24-10-2025
# Version 1

# Code that tests whether a valid input is given (v1)
'''done = False  # Boolean variable
while not done:
    num = int(input("Please enter your value: ")) # int() stores as a integer not a string
    done = True

print(f"The number that you entered is {num}")'''

# Code that tests whether a valid input is given (v1.1)
# Use the try and except method to catch errors
'''done = False
while not done:
    try: # This method tries for a valid input
        num = float(input("Please enter a integer: "))
        done = True

    except ValueError:
        print("That is not a valid float number. \n")

print(f"The number that you entered is {num}")'''

# Code that tests whether a valid input is given (v1.2)
# Create a function to call every time I ask the user for a number
# A function is a chunk of code that does something
# Functions can be used over and over again
# To use a function (call it), write out its name with paranthesis at the end
# To create a function, start with the word def(define)
'''def test_int_num():
    done = False
    while not done:
        try:
            num = float(input("Please enter your value: "))
            done = True

        except ValueError:
            print("That is not a valid float number. \n")

    print(f"The number that you entered is {num}")

# Main routine
test_int_num() # This calls the function so that we can use it'''

# Code that tests whether a valid input is given (v1.3)
# Use the function parameters to make my code more pythonic
'''def test_int(question): # 'question is a placeholder
    done = False
    while not done:
        error = "That is not a valid number. \n"
        print(question)
        try:
            num = int(input())
            done = True

        except ValueError:
            print(error)

    return(num) # Gives back the value of num so that I can use it outside of the function.

# Main routine
num1 = test_int("Please enter your first number: ")
print(f"Your first number is {num1}. \n")

num2 = test_int("Please enter your second number: ")
print(f"Your second number is {num2}. \n")

sum = num1 + num2
print(f"Your numbers added together is {sum}.")'''

# Code that tests whether a valid input is given (v1.4)
# Use the function parameters to make my code more pythonic
def valid_num(quesiton, low, high):
    error = f"Whoops! That's not an integer between {low} and {high}."
    while True:
        try:
            response = int(input(quesiton))
            # if response >= 0 and response <= 10:
            if low <= response <= high:
                break # This stops the loop

            else:
                print(f"{error} \n")

        except ValueError:
            print(f"{error} \n")

    return response # This makes the response available to be used

# Main routine

if __name__ == "__main__":
    num1 = valid_num("Enter your first number between 1 and 10: ", 1, 10)
    print(f"Your first number was {num1} \n")

    num2 = valid_num("Enter your second number between 11 and 20: ", 11, 20)
    print(f"Your second number was {num2} \n")

    num3 = valid_num("Enter your third number between 21 and 30: ", 21, 30)
    print(f"Your third number was {num3} \n")

    sum = num1 + num2 + num3
    print(f"Your numbers added together was {sum}. \n")

