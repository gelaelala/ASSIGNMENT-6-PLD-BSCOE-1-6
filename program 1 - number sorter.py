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
    if num1_ > num2_ and num1_ > num3_:
        return num1_
    elif num2_ > num3_ and num2_ > num4_:
        return num2_
    elif num3_ > num4_:
        return num3_
    else:
        return num4_

def secondhighest (num1_, num2_, num3_, num4_):
    if num2_ > num1_ and num2_ > num3_:
        return num2_
    elif num2_ < num3_:
        return num3_
    elif num2 > num4_:
        return num4_
    else:
        return num1_

def thirdhighest (num1_, num2_, num3_, num4_):
    max = num3_
    if num1_ > max:
        max = num1_
    elif num2_ > max:
        max = num2_
    else:
        max = num4_
    return max

def lowestnumber (num1_, num2_, num3_, num4_):
    if num1_ < num2_ and num1_ < num3_:
        return num1_
    elif num2_ < num3_ and num2_ < num4_:
        return num2_
    elif num3_ < num4_:
        return num3_
    else:
        return num4_

def displayorder (highestnumber_, secondhighest_, thirdhighest_, lowestnumber_):
    print (f'The order of the numbers you entered from highest to lowest is: {highestnumber_}, {secondhighest_}, {thirdhighest_}, {lowestnumber_}.')

num1, num2, num3, num4 = getnumbers()

highestnumber_ = highestnumber (num1, num2, num3, num4)

secondhighest_ = secondhighest (num1, num2, num3, num4)

thirdhighest_ = thirdhighest (num1, num2, num3, num4)

lowestnumber_ = lowestnumber (num1, num2, num3, num4)

displayorder (highestnumber_, secondhighest_, thirdhighest_, lowestnumber_)