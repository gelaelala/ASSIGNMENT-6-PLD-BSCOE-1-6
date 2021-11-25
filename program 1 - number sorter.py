# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement

def getnumbers():
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    number3 = float(input("Enter third number: "))
    number4 = float(input("Enter fourth number: "))
    return number1, number2, number3, number4

def sortnumber(num1_, num2_, num3_, num4_):
    if num1_ > num2_ and num1_ > num3_:
        if num2_ > num3_ and num3_ > num4_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num1_}, {num2_}, {num3_}, {num4_}. ')

num1, num2, num3, num4 = getnumbers()

sortnumber (num1, num2, num3, num4)