# Creating an input system for our coffee program
# Author: JJ Lee
# Date: 10-10-2025

# Version 1
# TODO: Ask the user if they like coffee
#       Record the answer
#       Give a response back to the answer

# Ask the user whether they like coffee or not
like_coffee = input("Do you like coffee? ")
print(f'your answer was "{like_coffee}".')

if like_coffee == "yes":
    print("That is great! I like coffee.")

else:
    print("You are missing out! Give it a try.")