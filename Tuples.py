# Topic 9: Question 1
t = (1,)

# Topic 9: Question 2
t+=([5,6],)

# Topic 9: Question 3
def det(M):
	return M[0][0] * M[1][1] - M[1][0]*M[0][1]

# Topic 9: Question 4
def hasSameContent(t1, t2):
	if len(t1) != len(t2):
		return False
	return sorted(t1)== sorted(t2)

# Topic 9: Question 5
def sumNumbers (*n):
	s=0
	for i in n :
		s+=i
	return s

# Topic 9: Question 6
def commonElements (n1,n2):
	r1=[]
	res=[]
	for i in n1 :
		r1.append(i)
	for j in n2 :
		r1.append(j)
	for k in range(len(r1)):
		if r1.count(r1[k]) > 1:
			if r1[k] in res:
				continue
			else:
				res.append(r1[k])
	return tuple(res)

# Topic 9: Question 7
def removeCommonElements (n1,n2):
    return tuple(sorted(set(n1) ^ set(n2)))

# Topic 9: Question 8
def shiftByTwo(*args) :
    return args[-2:]+args[:len(args)-2]

# Topic 9: Question 9
def sortByIndex (n):
    n.sort()
    r=[]
    for i in n :
        r.append( i[1])
    return tuple(r)

# Topic 9: Question 10
def sortByLength (t, order):
    r=()
    if order == 'asc':
        for i in (sorted(t,key=len)):
            r += (i,)
    elif order == 'des':
        for i in reversed(sorted(t,key=len)):
            r += (i,)
    return r
