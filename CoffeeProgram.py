# Creating an input system for our coffee program
# Author: JJ Lee
# Date: 10-17-2025

# Version 2
# TODO: Ask the user if they like coffee
#       Record the answer
#       Give a response back to the answer

# Version 1
# Ask the user whether they like coffee or not
'''like_coffee = input("Do you like coffee? ")
print(f'your answer was "{like_coffee}".')

if like_coffee == "yes":
    print("That is great! I like coffee.")

else:
    print("You are missing out! Give it a try.")'''

# Version 2
# While loop
# While loops let me test the program multiple times without clicking on run every time
'''keep_going = ""    # The variable contains an empty string
while keep_going == "":
    like_coffee = input("Do you like coffee? ")

    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee == "y" or like_coffee == "Y":
        print("That is great! I like coffee.")
        keep_going = "finished"

    elif like_coffee == "no" or like_coffee == "No" or like_coffee == "n" or like_coffee == "N":
        print("You are missing out! Give it a try.")
        keep_going = "finished"

    else:
        print("It's a yes or no question.")'''

# Version 3
# Make the program more pythonic
# Add "Do you like tea?"
keep_going = ""
while keep_going == "":
    # Convert answer to lowercase using .lower
    like_coffee = input("Do you like coffee? ").lower() # .lower converts to lowercase
    if like_coffee == "yes" or like_coffee == "y":
        print("That is great! I like coffee.")

    elif like_coffee == "no" or like_coffee == "n":
        print("You are missing out! Give it a try.")

        like_tea = input("Do you like tea instead? ").upper() # .upper converts to uppercase
        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee another try. :)")

        elif like_tea == "NO" or like_tea == "N":
            print("I am sorry. That's all I have for now")

        else:
            print("It's a yes or no question.")

    else: # Error message
        print("It's a yes or no question.")

    keep_going = input("Press <ENTER> to continue, or any other key to quit. Thanks!")
