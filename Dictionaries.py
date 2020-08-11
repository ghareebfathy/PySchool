# Topic 8: Question 1
contactinfo={}
contactinfo["Tom"] = {'Email':'tom@gmail.com', 'Phone':61234567}
contactinfo["Sally"]={'Email':'sally@hotmail.com', 'Phone':67654321}

# Topic 8: Question 2
d = { ["First", "Last"]: (1,3) }

# Topic 8: Question 3
'None of the above.'

# Topic 8: Question 4
d.values()

# Topic 8: Question 5
# Use a dictionary to provide the mapping of DNA to RNA bases.
def mRNAtranscription(dna_template):
    dna2rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    mRNA = ''
    for base in dna_template:
    	   mRNA+=dna2rna.get(base)


    return mRNA

# Topic 8: Question 6
def baseComposition(dna_seq):
	dna2rna = {'A':0,'T':0,'C':0,'G':0}
	for i in dna_seq:
		if i in dna2rna:
			dna2rna[i]+=1
	return(dna2rna)

# Topic 8: Question 7
def countLetters(word):
    y = 0
    r = dict.fromkeys(word,y)
    for i in word:
        if i in r:
            r[i]+=1

    return r

# Topic 8: Question 8
def reverseLookup(dictionary, value):
    r=[]
    for i in dictionary.keys():
        if dictionary[i] == value:
            r.extend(i)
    return sorted(r)

# Topic 8: Question 9
def invertDictionary(dictionary):
    newdict = {}
    for key, value in dictionary.items():
        newdict.setdefault(value, []).append(key)
    return newdict

# Topic 8: Question 10
def convertVector(numbers):
	d ={}
	count=0
	for i in numbers:
		if i !=0 :
		   d[count]=i
		count+=1
	return d

# Topic 8: Question 11
def convertDictionary(dictionary):
    if dictionary== {} :
        return []
    max_len = max(int(s)for s in dictionary.keys())
    return [dictionary.get(x,0)for  x in range(max_len+1)]

