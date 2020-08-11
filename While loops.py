# Topic 5: Question 1
def addNumbers(num):
    total = 0
    i = 1
    while i <=num:
    	total += i
    	i+=1
    return total

# Topic 5: Question 2

def addNumbers(start, end):
    total = 0
    while start <= end :
    	total += start
    	start+=1
    return total

# Topic 5: Question 3
10

# Topic 5: Question 4

def countPages(num):
    total = 0
    i = 1
    while i <= num:
         page_no = str(i)
	 total += page_no.count('1')
    	 i+=1
    return total

# Topic 5: Question 5
'All give the same output.'

# Topic 5: Question 6

def factorial(num):
    product = 1
    i = num
    while i > 0:
        product = product * i
        i -= 1

    return product

# Topic 5: Question 7

def doubleFactorial(num):
    product = 1
    i = 0
    k =  1
    while k < num:
       k = 2*i+1
       product *= k
       i += 1
    return product

# Topic 5: Question 8

def primeNumbers(num):
    primes = []
    i = 2
    # iterates through range from 2 to num(inclusive)
    while i <= num  :     # add 'while' condition
       k = 2
       isPrime = True
       # check if prime number
       while k  < i :      # add 'while' condition
	  if i%k==0:
	     isPrime = False
          k+=1            # update k
       if isPrime:
          primes.append(i)

       i +=1              # update i
    return primes

# Topic 5: Question 9

from math import floor

def sqApprox(num):
    fnum = int(floor(num))
    i = 0
    while True:
        if i * i <= fnum:
            minsq = i
        if i * i >= num:
            maxsq = i
            break
        i = i + 1
    assert minsq**2 <= num <= maxsq**2
    return minsq, maxsq

# Topic 5: Question 10

def piApprox(rank):
    value = 0
    for k in range(1, 2*rank+1, 2):
        sign = -(k % 4 - 2)
        value += float(sign) / k
    return 4 * value

# Topic 5: Question 11
def estimatePi():
        import math
        def factorial(n):
            if n == 0:
                return 1
            else:
                return math.factorial(n)

        k = 1
        Final = 0.31830987844
        while Final > 1e-15:
            b = (2 * math.sqrt(2) / 9801) * (factorial(4 * k) * (1103 + 26390 * k)) / (
                        (factorial(k) ** 4) * (396 ** (4 * k)))

            Final = Final + b
            k = k + 1
            return 1 / Final

# Topic 5: Question 12

def primeFactorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Topic 5: Question 13

from fractions import gcd # Python versions below 3.5
from functools import reduce # Python version 3.x
def LCM(nums):
      return reduce(lambda a,b: a*b // gcd(a,b), nums)

