from constant import *

print(LIST)

print("Here's a list of numbers")

# Prompt the user for input and convert it to an integer
user_input = int(input("The highest number in this list is?"))

x = max(5, 10, 11, 3, 4, 56, 25, 111, 25, 66)

if user_input == 111:
    print("Yes, that's correct")
else:
    print("That's not correct, it's", x)
    
LIST=5, 10, 11, 3, 4, 56, 25, 111, 25, 66
