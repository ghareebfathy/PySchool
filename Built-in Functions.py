# Topic 14: Question 1
# Write a function that returns 4 lists given a postive number.
def createLists(num):
    r=[]
    r1=[]
    for i in range(1,num+1):
        r1.append(i)
        r.append(-i)
    return (r1,r1[::-1],r[::-1],r)

# Topic 14: Question 2
# Write a function that returns the output as shown in the above examples.
def diff(a, b):
	r=  (a) + b
	if type(r) == complex:
		return abs(abs(r)+b)
	return abs(r)

# Topic 14: Question 3
# Write a function that returns a string of characters based on a list of ASCII codes.
def toString(alist):
    r = ''
    for i in alist:
        r += chr(i)
    return r

# Topic 14: Question 4
# Write a function that capitalizes the first character of each word.
def capitalize(phrase):
    r = phrase.split()
    r1=''
    for i in r :
        r1+= i.capitalize()+' '
    return r1.strip()

# Topic 14: Question 5
a = 10
b = 20
c = 0.0
d = 0.5

# Topic 14: Question 6
# Write a function that returns minimum and maximum values of a list containing numbers in integer and string formats.
def mixedList(mlist):
    r=[]
    for  i in mlist:
        r.append(int(i))
    return min(r),max(r)

# Topic 14: Question 7
a = 1.0
b = -1.0

# Topic 14: Question 8
# Write a function that converts a decimal integer to both hexadecimal and octal format.
def dec2hexoct(x):
    # return '%s'%hex(x), '0{0:o}'.format(x)
    return '0x%x'% x , '0%0o'% x

# Topic 14: Question 9
# Complete the code below so that the outputs are as shown in the examples above.
def mapfn1(alist):

    return list(map(hex,alist))

def mapfn2(alist):
    r = [x%2 for x in alist ]
    return list(map(lambda s:s  , r))

def mapfn3(word):
   return map(lambda word:word.upper(),  word)

# Topic 14: Question 10
# Complete the code below so that the outputs are as shown in the examples above.
def lowercase(x):
    r=[]
    for i in x :
        if  i.islower():
            r.append(i)
    return r
def fn1(word):
   return ''.join(list(filter(lowercase, word)))
def ones(x):
    r=''
    for i in x:
        if i in '0123456789':
            r+=(i)
    return r

def fn2(word):
   return ''.join(list(filter(lambda  s:s in ones(word) ,  word)))

# Topic 14: Question 11

# Write a factorial function using the 'reduce' function

def factorial(num):
    start = 1
    return reduce(lambda  a,b:a*b,range(1,int(num)+1),start)

# Topic 14: Question 12
c = zip(zip(a, b), zip(b, a))

# Topic 14: Question 13
'None of the above. '

# Topic 14: Question 14
# Write down the values of variables b and c, with the output as shown in the above example.

b = ('google')
c =('e','n','g','i','n','e')

# Topic 14: Question 15
tuple(1, 2, 3)

# Topic 14: Question 16
# Write a function that returns the total size of the arguments.
# Note: *args denotes a variable argument list, represented by a tuple.
def totSize(*args):
    r=0
    for i in args:
        r+=len(i)
    return r

# Topic 14: Question 17
# Write a function that returns the total of two sequences.
def totalSum(a, b):
    x = sum(a)
    y = sum(b)
    res= (x+y)
    return res

# Topic 14: Question 18
# Write a function that returns the exponent of a positive number given its base.
def exponent(num, base):
    a=0
    for i in range(1,num):
        if num % i == 0 :
            a+=1
    return a

# Topic 14: Question 19
# Write a function that checks if some or all of the items are true or false.
def checkItems(items):
    if all(items):
        return  'All are true.'
    if  any(items):
        return  'Some are true.'
    if  len(items) > 1 :
        return   'All are false.'

# Topic 14: Question 20
# Write a function that sorts a list of questions that are organized by 's'tage and
# 'q'uestion numbers.
def cmpqn(a):
     return len(a),a
def sortqns(qnlist):
    return sorted(qnlist, key = cmpqn)
