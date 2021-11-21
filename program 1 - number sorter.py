# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement

def getnumbers():
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    number3 = float(input("Enter third number: "))
    number4 = float(input("Enter fourth number: "))
    return number1, number2, number3, number4

def highestnumber(num1_, num2_, num3_, num4_):
    max = num1_
    if num2_ > max:
        max = num2_
    elif num3_ > max:
        max = num3_
    else:
        max = num4_
    return max


num1, num2, num3, num4 = getnumbers()

highestnumber_ = highestnumber (num1, num2, num3, num4)