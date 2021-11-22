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
    print (f"1. {num1} + {num2}")
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
    print (f"2. {num1} + {num2}")
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
    print (f'3. {num1} + {num2}')
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
    print (f'4. {num1} + {num2}')
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
    print (f'5. {num1} + {num2}')
    answer = int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct
    else:
        print ("Your answer is incorrect.")
        return incorrect

def sixth ():
    correct = int(1)
    incorrect = int(0)
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f'6. {num1} + {num2}')
    answer = int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct
    else:
        print ("Your answer is incorrect.")
        return incorrect

def seventh ():
    correct = int(1)
    incorrect = int(0)
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f'7. {num1} + {num2}')
    answer = int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct
    else:
        print ("Your answer is incorrect.")
        return incorrect

def eight ():
    correct = int(1)
    incorrect = int(0)
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f'8. {num1} + {num2}')
    answer = int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct
    else:
        print ("Your answer is incorrect.")
        return incorrect

def ninth ():
    correct = int(1)
    incorrect = int(0)
    num1 = (random.randint (0, 99))
    num2 = (random.randint (0, 99))
    print (f'9. {num1} + {num2}')
    answer = int(input("Enter answer: "))
    time.sleep (1)
    if answer == num1 + num2:
        print ("Your answer is correct.")
        return correct
    else:
        print ("Your answer is incorrect.")
        return incorrect


def displayresult (num1, num2, num3, num4, num5, num6, num7, num8, num9):
    result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
    time.sleep(1)
    print (f"Based from the results, your total score is {result}/9.")
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

time.sleep (2)

number6 = sixth ()

time.sleep (2)

number7 = seventh ()

time.sleep (2)

number8 = eight ()

time.sleep (2)

number9 = ninth ()

results = displayresult (number1, number2, number3, number4, number5, number6, number7, number8, number9)