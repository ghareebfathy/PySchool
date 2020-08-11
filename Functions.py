# Topic 2: Question 1
def addNumber(x, y):
	return x + y

# Topic 2: Question 2

def subtractNumber(x, y):
	return x - y

# Topic 2: Question 3

def getBiggerNumber(x, y):
    if x > y:
        return x
    else:
        return y

# Topic 2: Question 4

import math
# Calculate the square root of 16 and stores it in the variable a
a = math.sqrt(16)

# Calculate 3 to the power of 5 and stores it in the variable b
b =math.pow(3,5)

# Calculate area of circle with radius = 3.0 by making use of the math.pi constant and store it in the variable c
c = math.pi*9

# Topic 2: Question 5

# Note: Return a string of 2 decimal places.
def Cel2Fah(temp):
	fahrenheit = (temp * 9 /5)+32
	return ('%0.02f' %(fahrenheit))

# Topic 2: Question 6

# Note: Return a string of 1 decimal place.
import math
def BMI(weight, height):
	bmi = float(weight)/(height*height)
    	return '%.1f' % bmi

# Topic 2: Question 7

def percent( a, b):
    return int((float(a) / b) * 100)

# Topic 2: Question 8
import math
def hypotenuse(a, b):
	c= math.sqrt((a*a)+(b*b))
	return int(c)

# Topic 2: Question 9

def getSumOfLastDigits(numList):
    result = 0

    for i in numList:
        x = str(i)[-1]
        result += int(x)
    return result

# Topic 2: Question 10
def introduce(name, age=0):

    msg = "My name is %s. " % name
    if age == 0:
       msg += "My age is secret."
    else:
       msg += "I am %d years old." % age
    return msg

# Topic 2: Question 11

def isEquilateral(x, y, z):
    if x and y and z > 0:
        if x == y and x == z:
            return True
    return False

# Topic 2: Question 12

def quadratic(a, b, c):
    D = (b ** 2) - (4 * a * c)
    return ('The discriminant is {0}.'.format(D))

# Topic 2: Question 13

def addFirstAndLast(x):
	if len(x)== 0 :
		return 0
	elif len(x) > 1:
		return x[0]+x[-1]
	else:
		return x[0]

# Topic 2: Question 14

# Complete the 'lambda' expression so that it returns True if the argument is an even number, and False otherwise.
even = lambda x:x % 2 == 0

# Topic 2: Question 15

def getScore(data):
    'A function that computes and returns the final score.'
    return data
# Topic 2: Question 16

def addOne(x):
    return x + 1

def useFunction(func, num):
    return func(num) ** 2

# Topic 2: Question 17

import math

def calDistance(x1, y1, x2, y2):
    return math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1))
