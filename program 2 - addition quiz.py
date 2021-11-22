# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random 
import time

def first ():
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f"{num1} + {num2}")
    answer =  int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        if print ("Correct"):
            return answer
    else:
        print ("Incorrect")

def second ():
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f"{num1} + {num2}")
    answer =  int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        if print ("Correct"):
            return answer
    else:
        print ("Incorrect")

first ()

time.sleep (1)

second ()