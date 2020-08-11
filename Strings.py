# Topic 7: Question 1
def countA(word):
	if 'a' in word:
		return word.count('a')
	else:
		return 0

# Topic 7: Question 2
def countLetter(word, letter):
	if letter  in word:
		return word.count(letter)
	else:
		return 0

# Topic 7: Question 3
def removeLetter(word, letter):
    r=[]
    for i in word:
        r.append(i)
        if letter in r :
            r.remove(letter)
    return ''.join(r)

# Topic 7: Question 4
def changeCase(word):
        return word.swapcase()

# Topic 7: Question 5
def search(word, substring):
    if substring in word:
        return len(substring)
    else:
        return -1

# Topic 7: Question 6
def getChar(word, pos):
    if pos > len(word):
        return 'Invalid Range.'
    else:
        return word[pos]

# Topic 7: Question 7
def countVowels(word):
    a=('a', 'e', 'i', 'o', 'u')
    r=[]
    s=0
    for i in a:
        r.append(word.count(i))
    for i in r:
        s+=i
    return s

# Topic 7: Question 8
def getVowels(word):
    a = ('a', 'e', 'i', 'o', 'u')
    r=[]
    for i in word:
       if i.lower() in a:
            r.append(i)

    return r

# Topic 7: Question 9
def capitalizeVowels(word):
        return ''.join(c.upper() if c in 'aeiou' else c for c in word)

# Topic 7: Question 10
def startEndVowels(word):
    vowels = tuple("aeiouAEIOU")
    return word.startswith(vowels) and word.endswith(vowels)

# Topic 7: Question 11
def removeVowels(word):
    vowels = tuple("aeiouAEIOU")
    res=[]
    string =[]
    for i in word:
        if i in vowels:
            res.append(i)
    for i in word:
        string.append(i)
    for i in res:
        string.remove(i)
    return ''.join(string)

# Topic 7: Question 12
def reverseWord(word):
	return word[::-1]

# Topic 7: Question 13
def isReverse(word1, word2):
    if word1 == word2[::-1]:
        return True
    else:
        return False

# Topic 7: Question 14
def startWithVowel(word):
    vowels = tuple("aeiouAEIOU")
    for i in range(len(word)):
        if word[0] in vowels:
            return word
        if word[0][i] not in  vowels and  word[-1][i]  not in vowels:
            return  'No vowel'
        else:
            return word[1::]

# Topic 7: Question 15
def getCommonLetters(word1, word2):
    r1 = []
    r2 = []
    for i in word1:
        for j in word2:
            if i == j:
                r1.append(i)
    for i in r1:
        if i not in r2:
            r2.append(i)

    r2 = sorted(r2)
    return ''.join(r2)

# Topic 7: Question 16
def mirrorText(word1, word2):
    return word1+word2*2+word1

# Topic 7: Question 17
def echoWord(word):
    return len(word)* word

# Topic 7: Question 18
def rightJustify(word):
    return "%50s" % word

# Topic 7: Question 19
def isPalindrome(word):
    r = []
    r2 = []
    r.append(str(word))
    r2.append(str(word))
    r3 = r2[::-1]
    for i in range(len(r)):
        if r[i] == r3[i] and len(r[i]) > 0:
            return True
        else:
            return False
# Topic 7: Question 20
def isInAlphabeticalOrder(word):
    word_r=[]
    word_sort=[]
    for i in word:
        word_r.append(i)
        word_sort.append(i)
    s = sorted(word_sort)
    if word_r == s:
        return True
    else:
        return False

# Topic 7: Question 21
def isAllLettersUsed(word, required):
    w=[]
    re=[]

    for k in word:
        w.append(k)
    for j in required:
        re.append(j)
    for i in range(len(word)):
        if re[i] in w:
            return True
        else:
            return False

# Topic 7: Question 22
def isTripleDouble(word):
    y = 0
    x= 0
    r = dict.fromkeys(word,y)
    for i in word:
        if i in r:
            r[i]+=1
    a = list(r.values())
    b= [2,2,2]

    if a[0:]== b[0:3] or a[1:]== b[0:3]:
        return True
    else:
        return False

# Topic 7: Question 23
def splitWord(word, numOfChar):
    r = []
    for i in range(0, len(word), numOfChar):
        r.append(word[i:i + numOfChar])
    return r

# Topic 7: Question 24
def isAnagram(w1, w2):
    w1=w1.lower()
    w2=w2.lower()
    if w1[0:2]==w2[0:2] and w1[-2:]==w2[-2:]:
        return True
    else:
        return False

