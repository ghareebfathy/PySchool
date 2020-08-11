# Topic 11: Question 1
def factorial(n):
    factorial = 1

    if n >= 1:
    	for i in range (1,int(n)+1):
   		factorial = factorial * i
        return factorial
    else:
        return 1

# Topic 11: Question 2
def power(x, y):
    if y == 0:
        return 1
    else:
        return x ** y

# Topic 11: Question 3
def fibonacci(n):
    r=1
    if n == 0:
        return 0
    if n == 1 :
        return 1
    if n > 1:
        for i in range(1,int(n)+1):
            r = fibonacci(i-1) + fibonacci(i-2)
    return r

# Topic 11: Question 4
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

# Topic 11: Question 5

# Hint: (1) Check if the first and last characters are equal.
#       (2) Repeat step 1 recursively on its substrings (with first and last characters removed).
def isPalindrome(word):
    r1 = word.lower()
    r2= (r1[::-1])
    if r1 == r2 :
        return True
    else:
        return False

# Topic 11: Question 6

def sumOfDigits(num):
    r= str(num)
    reslut = 0
    for i in r:
        reslut+=int(i)
    return reslut

# Topic 11: Question 7
# You can use this code segment as template or rewrite everything on your own
def countX(s):
	n=0
	for i in s:
		if 'X' in i:
			n+=1
	return n

# Topic 11: Question 8

# You can use this code segment as template or rewrite everything on your own
# Replace the _BLANK_ with your own code
def addDashes(s):
    r=''
    if len(s)> 1:
        for i in s:
            r +=i+'-'
        return r[0:-1:]
    elif len(s)== 1:
        return s
    else:
        return None

# Topic 11: Question 9
# You can use this code segment as template or rewrite everything on your own
# Replace the _BLANK_ with your own code

def sumNumbersFromOne(x):
    result = 0
    if x > 0 :
        for i in range(x+1):
            result+=i
    else:
        return 'Invalid'
    return result

# Topic 11: Question 10

# You can use this code segment as template or rewrite everything on your own
# Replace the _BLANK_ with your own code
def numbersInbetween(a, b):
    if b < a:
        return "Invalid"
    if a == b:
        return '%d' % (a)
    else:
        return '%s,%s' % (a, numbersInbetween(a+1,b))

# Topic 11: Question 11

# You can use this code segment as template or rewrite everything on your own
# Replace _BLANK_ with your code

def createStars(x):
    if x == 0:
        return '*'

    else:
        return createStars(x - 1) * 2

# Topic 11: Question 12

# You can use this code segment as template or rewrite everything on your own
# Replace _BLANK_ with your code

def createPattern(x):
    if x == 0:
        return ''
    if x == 1:
        return '*'
    if x == 2:
        return '**'
    elif x % 2 == 0:
        return '<' + createPattern(x - 2) + '>'
    elif x == 3:

        return "<" + createPattern(x - 2) + ">"
    else:
        if x % 2 == 1:
            return "<" + createPattern(x - 2) + ">"

# Topic 11: Question 13
def printTwos(n):
    if n % 4 != 0:
        if n % 2 == 0:
            result = printTwos(int(n/2))
            return "2 * " + str(result)
        else:
            return str(n)
    else:
        result = printTwos(int(n/4))
        return "2 * %s * 2" % str(result)

# Topic 11: Question 14

# Note: Row and column are counting from 0, i.e. coordinates of top element is (0, 0).
def pascal(row, col):
    res = 1
    if (col > row - col):
        col = row - col
    for i in range(0,col):
        res = res * (row - i)
        res = res // (i+1)
    return res
