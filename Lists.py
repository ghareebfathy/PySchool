# Topic 6: Question 1
aList = ['Hello',0, 20.0,'World']

# Topic 6: Question 2
aList = ['Hello', 0]
aList[1:3]=[0, 20.0]
aList.append('World')

# Topic 6: Question 3
aList = ['hello', 'i', 'love', 'python', 'programming']
del aList[1]
del aList[1]

# Topic 6: Question 4
def addNumbersInList(numbers):
	return sum(numbers)

# Topic 6: Question 5
def addOddNumbers(numbers):
	res=[]
	for i in range(len(numbers)):
		if numbers[i] % 2== 1:
			res.append( numbers[i])
	return sum(res)

# Topic 6: Question 6
def countOddNumbers(numbers):
	res=[]
	for i in range(len(numbers)):
		if numbers[i] % 2== 1:
			res.append( numbers[i])
	return len(res)

# Topic 6: Question 7
def getEvenNumbers(numbers):
	res=[]
	for i in range(len(numbers)):
		if numbers[i] % 2== 0:
			res.append( numbers[i])
	return (res)

# Topic 6: Question 8
def removeFirstAndLast(numbers):
	if len(numbers)== 0:
		return
	else:
		del numbers[0]
	if len(numbers) <= 0:
		return numbers
	else:
		del numbers[-1]
        return numbers

# Topic 6: Question 9
def getMaxNumber(numbers):
	if len(numbers) > 1:
		n = max(numbers)
	else:
		n = 'N.A'
	return n

# Topic 6: Question 10
def getMinNumber(numbers):
	if len(numbers) > 1:
		n = min(numbers)
	else:
		n = 'N.A'
	return n

# Topic 6: Question 11
def MatrixProduct(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print ("Cannot multiply the two matrices. Incorrect dimensions.")
      return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    print(C)

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Topic 6: Question 12
a = [1,2,3]
a.append(4)

# Topic 6: Question 13
def matrixDimensions(m):
    re=[]
    for i in range(len(m)):
        re.append(len(m[i]))
    eq= re[0] == re[-1]
    if eq is False:
        return 'This is not a valid matrix.'

    else:
        return('This is a {}x{} matrix.'.format(len(re),re[0] ))

# Topic 6: Question 14
a = [1, 5, 3]
b = [1, 5, 3]

# Topic 6: Question 15
a = [4, 5, 3]
b = [1, 5, 6]

# Topic 6: Question 16
def combine(la, lb):
    r_num =[]
    r_str =[]

    for i in la:
        if type(i) is int :
            r_num.append(i)
        else:
            r_str.append(i)
    for j in lb:
        if type(j) is int :
            r_num.append(j)
        else:
            r_str.append(j)
    r_num.sort()
    r_str.sort()
    r_num.extend(r_str)
    # return  r_num ,' ',r_str
    return (r_num)

# Topic 6: Question 17
def transpose(matrix):
    r = []
    for i in zip(*matrix):
        r.append(list(i))
    return r

# Topic 6: Question 18

[1, 1, 2, 2, 2, 2, 2, 2]

# Topic 6: Question 19
def calCumulativeSum(numbers):
    r=[]
    a=0
    for i in numbers:
        a+=i
        r.append(a)
    return r

# Topic 6: Question 20
def combineList(list1, list2):
    r= []
    r1=[]
    for i in list1:
        r .append(i)

    for j  in  list2:
        r1.append(j)
    r.extend(r1)

    return (r)

# Topic 6: Question 21
def subtractList(list1, list2):
    r=[]
    for n in list1:
        if n not in list2:
            r.append(n)
    return r

# Topic 6: Question 22
def countLetters(word) :

    r=[]
    r1=[]
    r2=[]
    r3=[]
    for w in word:
        r.append(word.count(w))
    for num in range(len(word)):
        r1.append(word[num])
    for i in zip(r1,r):
        r2.append(i)
    for i in r2:
        if i not in r3:
            r3.append(i)

    return sorted(r3)

# Topic 6: Question 23
def getNumbers(num):
    odd=[]
    even=[]
    r=[]
    r2=[]
    if num % 2 == 0:
        for i in range(num+1):
            if i % 2 == 0:
                even.append(i*i)
        r.extend(even[::-1])
        r.extend(even[1::])
        return r

    if num % 2 == 1:
        for i in range(num+1):
            if i % 2 == 1:
                odd.append(i*i)
        r2.extend(odd[::-1])
        r2.extend(odd[::])
        return r2

# Topic 6: Question 24
def getSumOfFirstDigit(num):
    l=[]
    s = 0
    for m in num:
        l.append(str(m))
    for i in l:
        s += int(i[0])
    return s

# Topic 6: Question 25
a = [[ ]]
b = [0, [0], 0]

# Topic 6: Question 26
def getAboveAverage(nums):
	r=[]
	nums=sorted(nums)
	for i in nums:
		if i > 0 :
			r.append(i)
	return r[-2:]
