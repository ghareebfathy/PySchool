# Topic 4: Question 1
def generateNumber(num):
    res = []
    for i in range(0, num + 1):
        res.append(i)
    return res

# Topic 4: Question 2
def generateNumber(start, end):
    res = []
    for i in range(start, end + 1):
        res.append(i)
    return res

# Topic 4: Question 3

def generateNumber(start, end, step):
    res = []
    if step < 0:
        for i in range(start, end - 1, step):
            res.append(i)
    else:
        for i in range(start, end + 1, step):
            res.append(i)

    return res

# Topic 4: Question 4

def addNumbers(num):
	for i in range(num):
		num+=i
	return num

# Topic 4: Question 5

def addNumbers(start,end):
	res=[]
	for i in range(start,end+1):
		res.append(i)
	return sum(res)

# Topic 4: Question 6

def addEvenNumbers (start,end):
	res=[]
	for i in range(start , end+1):
		if i % 2 == 0:
			res.append(i)
	return sum(res)

# Topic 4: Question 7

def skipVowels(word):
    novowels = ''
    for ch in word:
        if ch.lower() in 'aeiou':
           continue
           novowels += ch
        novowels+=ch
    return novowels

# Topic 4: Question 8

def stripComment(sentence):
    codeonly  = ""
    for ch in sentence:
        if ch == '#':
           break
	   codeonly += '#'
        codeonly+=ch
    return codeonly

# Topic 4: Question 9

def genSet(nums):
	res=[]
	for i in nums:
		if i not in res:
			res.append(i)
	res.sort()
	return res

# Topic 4: Question 10
greetings = 'Hello World'
for x in greetings:
    print (greetings[x],)

# Topic 4: Question 11

def sumOfDigit (num):
	res=[]
	num=str(num)
	for i in num:
		res.append(int(i))
	return sum(res)

