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

def sortnumber2(num1_, num2_, num3_, num4_):
            if num1_ > num2_ and num1_ > num3_:
                if num2_ > num3_ and num2_ > num4_:
                    if num4_ > num3_:
                        print (f'The order of the numbers that you entered, from highest to lowest, is {num1_}, {num2_}, {num4_}, {num3_}. ')

def sortnumber3(num1_, num2_, num3_, num4_):
            if num1_ > num2_ and num1_ > num3_:
                if num3_ > num2_ and num2_ > num4_:
                        print (f'The order of the numbers that you entered, from highest to lowest, is {num1_}, {num3_}, {num2_}, {num4_}. ')

def sortnumber4(num1_, num2_, num3_, num4_):
            if num1_ > num4_ and num1_ > num2_:
                if num4_ > num2_ and num2_ > num3_:
                        print (f'The order of the numbers that you entered, from highest to lowest, is {num1_}, {num4_}, {num2_}, {num3_}. ')

def sortnumber5(num1_, num2_, num3_, num4_):
            if num1_ > num4_ and num1_ > num3_:
                if num4_ > num3_ and num3_ > num2_:
                        print (f'The order of the numbers that you entered, from highest to lowest, is {num1_}, {num4_}, {num3_}, {num2_}. ')

def sortnumber6(num1_, num2_, num3_, num4_):
    if num2_ > num1_ and num2_ > num3_:
        if num1_ > num3_ and num3_ > num4_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num2_}, {num1_}, {num3_}, {num4_}.')

def sortnumber7 (num1_, num2_, num3_, num4_):
    if num2_ > num1_ and num2_ > num4_:
        if num1_ > num4_ and num4_ > num3_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num2_}, {num1_}, {num4_}, {num3_}.')

def sortnumber8 (num1_, num2_, num3_, num4_):
    if num2_ > num3_ and num2_ > num1_:
        if num3_ > num1_ and num1_ > num4_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num2_}, {num3_}, {num1_}, {num4}.')

def sortnumber9 (num1_, num2_, num3_, num4_):
    if num2_ > num3_ and num2_ > num4_:
        if num3_ > num4_ and num4_ > num1_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num2_}, {num3_}, {num4_}, {num1_}.')

def sortnumber10 (num1_, num2_, num3_, num4_):
    if num2_ > num4_ and num2_ > num1_:
        if  num4_ > num1_ and num1_ > num3_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num2_}, {num4_}, {num1_}, {num3_}.')

def sortnumber11 (num1_, num2_, num3_, num4_):
    if num2_ > num4_ and num2_ > num3_:
        if num4_ > num3_ and num3_ > num1_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num2_}, {num4_}, {num3_}, {num1_}.')

def sortnumber12 (num1_, num2_, num3_, num4_):
    if num1_ > num3_ and num1_ > num4_:
        if num3_ > num4_ and num4_ > num2_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num1_}, {num3_}, {num4_}, {num2_}.')

def sortnumber13 (num1_, num2_, num3_, num4_):
    if num3_ > num1_ and num3_ > num2_:
        if num1_ > num2_ and num2_ > num4_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num3_}, {num1_}, {num2_}, {num4_}.')

def sortnumber14 (num1_, num2_, num3_, num4_):
    if num3_ > num1_ and num3_ > num4_:
        if num1_ > num4_ and num4_ > num2_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num3_}, {num1_}, {num4_}, {num2_}.' )

def sortnumber15 (num1_, num2_, num3_, num4_):
    if num3_ > num2_ and num3_ > num1_:
        if num2_ > num1_ and num1_ > num4_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num3_}, {num2_}, {num1_}, {num4_}.')

def sortnumber16 (num1_, num2_, num3_, num4_):
    if num3_ > num2_ and num3_ > num4_:
        if num2_ > num4_ and num4_ > num1_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num3_}, {num2_}, {num4_}, {num1_}.')

def sortnumber17 (num1_, num2_, num3_, num4_):
    if num3_ > num4_ and num3_ > num1_:
        if num4_ > num1_ and num1_ > num2_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num3_}, {num4_}, {num1_}, {num2_}.')

def sortnumber18 (num1_, num2_, num3_, num4_):
    if num3_ > num4_ and num3_ > num2_:
        if num4_ > num2_ and num2_ > num1_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num3_}, {num4_}, {num2_}, {num1_}.')

def sortnumber19 (num1_, num2_, num3_, num4_):
    if num4_ > num1_ and num4_ > num2_:
        if num1_ > num2_ and num2_ > num3_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num4_}, {num1_}, {num2_}, {num3_}.')

def sortnumber20 (num1_, num2_, num3_, num4_):
    if num4_ > num2_ and num4_ > num1_:
        if num2_ > num1_ and num1_ > num3_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num4_}, {num2_}, {num1_}, {num3_}.')

def sortnumber21 (num1_, num2_, num3_, num4_):
    if num4_ > num2_ and num4_ > num3_:
        if num2_ > num3_ and num3_ > num1_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num4_}, {num2_}, {num3_}, {num1_}.')

def sortnumber22 (num1_, num2_, num3_, num4_):
    if num4_ > num3_ and num4_ > num1_:
        if num3_ > num1_ and num1_ > num2_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num4_}, {num3_}, {num1_}, {num2_}.')

def sortnumber23 (num1_, num2_, num3_, num4_):
    if num4_ > num3_ and num4_ > num2_:
        if num3_ > num2_ and num2_ > num1_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num4_}, {num3_}, {num2_}, {num1_}.')

def sortnumber24 (num1_, num2_, num3_, num4_):
    if num4_ > num1_ and num4_ > num3_:
        if num1_ > num3_ and num3_ > num2_:
            print (f'The order of the numbers that you entered, from highest to lowest, is {num4_}, {num1_}, {num3_}, {num2_}.')

num1, num2, num3, num4 = getnumbers()

sortnumber (num1, num2, num3, num4)

sortnumber2 (num1, num2, num3, num4)

sortnumber3 (num1, num2, num3, num4)

sortnumber4 (num1, num2, num3, num4)

sortnumber5 (num1, num2, num3, num4)

sortnumber6 (num1, num2, num3, num4)

sortnumber7 (num1, num2, num3, num4)

sortnumber8 (num1, num2, num3, num4)

sortnumber9 (num1, num2, num3, num4)

sortnumber10 (num1, num2, num3, num4)

sortnumber11 (num1, num2, num3, num4)

sortnumber12 (num1, num2, num3, num4)

sortnumber13 (num1, num2, num3, num4)

sortnumber14 (num1, num2, num3, num4)

sortnumber15 (num1, num2, num3, num4)

sortnumber16 (num1, num2, num3, num4)

sortnumber17 (num1, num2, num3, num4)

sortnumber18 (num1, num2, num3, num4)

sortnumber19 (num1, num2, num3, num4)

sortnumber20 (num1, num2, num3, num4)

sortnumber21 (num1, num2, num3, num4)

sortnumber22 (num1, num2, num3, num4)

sortnumber23 (num1, num2, num3, num4)

sortnumber24 (num1, num2, num3, num4)