# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random 
import time

def first ():
    correct = int(1)
    incorrect = int(0)
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f"{num1} + {num2}")
    answer =  int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct
    else:
        print ("Your answer is incorrect.")
        return incorrect

def second ():
    correct = int(1)
    incorrect = int(0)
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f"{num1} + {num2}")
    answer =  int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct
    else:
        print ("Your answer is incorrect.")
        return incorrect

def third ():
    correct = int(1)
    incorrect = int(0)
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f'{num1} + {num2}')
    answer = int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct
    else:
        print ("Your answer is incorrect.")
        return incorrect

def fourth ():
    correct = int(1)
    incorrect = int(0)
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f'{num1} + {num2}')
    answer = int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct 
    else:
        print ("Your answer is incorrect.")
        return incorrect

def fifth ():
    correct = int(1)
    incorrect = int(0)
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f'{num1} + {num2}')
    answer = int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct
    else:
        print ("Your answer is incorrect.")
        return incorrect

def displayresult (first_, second_, third_, fourth_, fifth_):
    result = first_ + second_ + third_ + fourth_ + fifth_ 
    time.sleep(1)
    print (f"Based from the results, your total score is {result}/5.")
    time.sleep (1)
    print ("Thank you for joining the quiz!")

number1 = first ()

time.sleep (2)

number2 = second ()

time.sleep (2)

number3 = third ()

time.sleep (2)

number4 = fourth ()

time.sleep (2)

number5 = fifth ()

results = displayresult (number1, number2, number3, number4, number5)