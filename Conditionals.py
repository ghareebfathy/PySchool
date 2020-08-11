# Topic 3: Question 1

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

# Topic 3: Question 2

def isIsosceles(x, y, z):
	l = [x, y, z]
	for a in l:
		for b in l:
			if a <= 0:
				return False
			elif a == b:
				if x == y or x == z:
					return True
			else:
				return False

# Topic 3: Question 3

def isScalene(x, y, z):
    if x != y and x != z and y != x and y != z and z != y and z != x:
        return True
    else:
        return False

# Topic 3: Question 4

def Fitness(a,b,c):
    f = [a,b,c]
    total = sum(f)
    smallest = min(f)
    if smallest >= 4 and total >= 13:
        return ('Gold')
    elif smallest >= 3 and total >= 10:
        return ('Silver')
    elif smallest >= 2 and total >= 7:
        return ('Pass')
    else:
        return ('Fail')

# Topic 3: Question 5

# Hint: Step through the range between (2, number-1),
# and determine if the number is divisible using the modulus operator.
def isPrime(x):
    if x <= 1:
        return False
    for d in range(2, x):
        if x % d == 0:
            return False
    return True

# Topic 3: Question 6

import math


def HealthScreen(weight, height):
    BMI = weight / (height * height)
    if BMI > 27.5:
        return 'Your BMI is %.1f (High Risk).' % (BMI)
    elif BMI > 23 and BMI < 27.4:
        return 'Your BMI is %.1f (Moderate Risk).' % (BMI)
    elif BMI > 18.5 and BMI < 22.9:
        return 'Your BMI is %.1f (Low Risk).' % (BMI)
    else:
        return 'Your BMI is %.1f (Risk of nutritional deficiency diseases).' % (BMI)

# Topic 3: Question 7

def isTriangle(x,y,z):
	l= (x+y+z)
	if l % 3 == 0:
		if (x+y)> z:
			return True
		else:
			return False
	return False

# Topic 3: Question 8

def quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return "This equation has 2 complex roots."
    elif d > 0:
        return "This equation has 2 real roots."
    else:
        return "This equation has 1 real root."

# Topic 3: Question 9

def time24hr(s):
    c = s.split(':')
    h = int(c[0])
    m = int(c[1][0:-2])
    h = h % 12 if s[-2:] != 'pm' else 12 if h == 12 else h + 12
    return "%02d%02dhr" % (h, m)

# Topic 3: Question 10

def LeapYear(yr):
	if yr % 4 == 0  and yr % 100 !=0 :
		return True
	else:
		return False

# Topic 3: Question 11

def pairwiseScore(seqA, seqB):
	h = []
	c = []
	for x in range(0,len(seqA)):
		if seqA[x] == seqB[x]:
			h.append('|')
		else:
			h.append(' ')
		if len(h) > 1:
			if h[x] == '|':
				if h[x] == h[x-1]:
					c.append(3)
				else:
					c.append(1)
			elif h[x] == ' ':
				c.append(-1)
		else:
			if h[x] == '|':
				c.append(1)
			elif h[x] == ' ':
				c.append(-1)
	a = "".join(h)
	return "".join((seqA, '\n', a, '\n', seqB, '\n', 'Score: %d' % sum(c)))

# Topic 3: Question 12

def RiskGame(attacker, defender):
    attacker.sort(reverse=True)
    defender.sort(reverse=True)
    pairs = zip(attacker, defender)
    for a, d in pairs:
        if a :
            if a > d :
               return 'Defender loses 2 armies.'
            elif a == d :
                return  'Attacker loses 2 armies.'
            else:
                return  'Attacker loses 1 army and defender loses 1 army.'
        return  'Attacker loses 1 army and defender loses 1 army.'

# Topic 3: Question 13

def tictactoe(moves):
    for r in range(len(moves)):
        for c in range(len(moves[r])):
            if moves[0][c]==moves[1][c]==moves[2][c]:
                return "\'%s\' wins (%s)." % ((moves[0][c]),'vertical')
            elif moves[r][0]==moves[r][1]==moves[r][2]:
                return "\'%s\' wins (%s)."%((moves[r][0]),'horizontal')
            elif moves[0][0]==moves[1][1]==moves[2][2]:
                return "\'%s\' wins (%s)."%((moves[0][0]),'diagonal')
            elif moves[0][2]==moves[1][1]==moves[2][0]:
                return "\'%s\' wins (%s)."%((moves[0][2]),'diagonal')
    return 'Draw.'

# Topic 3: Question 14

def time12hr(t):
    hour = int(t[0:2])
    if hour > 12:

        return ('{}:{} {}'.format(hour - 12, (t[-2:]), 'p.m.'))
    elif hour == 12:
        return ('{}:{} {}'.format(hour, (t[-2:]), 'p.m.'))
    else:

        return ('{}:{} {}'.format(hour + 12, (t[-2:]), 'a.m.'))

