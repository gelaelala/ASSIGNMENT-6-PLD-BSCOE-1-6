# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random 

def first ():
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f"{num1} + {num2}")
    answer =  int(input("Enter answer: "))
    if answer == num1 + num2:
        print ("Correct")
    else:
        print ("Incorrect")

first ()