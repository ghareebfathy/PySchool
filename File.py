# Topic 13: Question 1
# Create a file called 'tmp.txt' for writing, and close the file after that.

# open a file
f = open('tmp.txt','a')  # replace 'filename' and 'mode'

# write to file
f.write('hello')

# close a file
f.close()
f.closed

# Topic 13: Question 2
# Create a function that appends the name and email to the end of a named file.
def addEmail(filename, name, email):
    f = open(filename, mode='a')  # replace the mode

    # Append name and email, each record should end with '\n'.
    f.write("%s"%(name))
    f.write(" %s\n"%email)
    # close file
    f.close()
    return f  # do not remove this line

# Topic 13: Question 3
seq = [1, 2, 3, 4]

# Topic 13: Question 4

# Write a function that open a file for reading and returns the number of bytes and newlines('\n').
def readFile(filename):
    f = open(filename)
    size = 0
    lines = 0
    while 1:
        char = f.read(1)
        if not  char :
            break
        size+=1
        if (char == "\n"):
            lines+=1
    f.close()

    return (size, lines)

# Topic 13: Question 5
# Use seek() and read() methods to retrieve a hidden code from a list of indexes.
# A negative index implies searching from the end of document.
def getCode(filename, indexes):
    r = ''
    r1 = []
    f = open(filename, 'r')

    r += f.read()
    for i in indexes:
        if i > 0:
            r1.append(r[i])
        else:
            r1.append(r[i])
    return ''.join(r1)

# Topic 13: Question 6
# The test score of the students in a class is stored in a file in the
# following format:
#
# Name    Score
# John    89
# Susan   85
#
# Write a function to read the scores and compute the average score of the
# class. (Ignore the first line which contains the field headers).
def getMean(filename):
    f = open(filename)
    scnt = total = 0  # initialize student counter and total score

    line = f.readline()  # read first line, do nothing
    line = f.readline()  # read 2nd line
    while line.rstrip() != "":  # check for empty line or EOF

        tokens = line.split()  # split line into tokens, tokens[0] is name
        total += int(tokens[1])  # add score
        scnt += 1.  # update student counter
        line = f.readline()  # read next line

    return "Average Score: %.2f" % (total / scnt)

# Topic 13: Question 7
# In a competition, the average score of a contestant is computed after discarding the best
# and worst scores. Write a function that returns the average scores of the gold medalist.
# The raw scores of each contestant is stored in a file in the following format:
# Li Ning, 9.8 9.7 9.6 9.3 9.4, 9.8
# Millman, 9.8 9.2 9.1 9.0 9.4, 9.5 9.1
#

def getWinner(filename):
    results = open(filename).readlines()
    winner = ''
    max_score =0
    for line in results:
        tokens = line.split(',')
        name =  tokens[0]
        scores = sorted(map(float, tokens[1].split()))
        ave = sum(scores[1:-1])/(len(scores) - 2)
        if ave > max_score:
           winner = name
           max_score = ave
    return "%s [%.1f]" % (winner, max_score)

# Topic 13: Question 8

# Write a function to read a CSV file with ',' as delimiter and returns a list of records.
# The function must be able to ignore ',' that are within a pair of double quotes '"'.
import csv
def csvReader(filename):
    records = []
    with open(filename,'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            # line = line.strip('\n')  # strip '\n'
            if line=='':
               continue           # ignore empty line
            records.append(line)
        f.close()
    return records

# Topic 13: Question 9

# Note: The field headers are sorted in alphabetical order.
import csv

def csvWriter(filename, records):
    header = []
    f = []
    with open(filename, 'w')as new_file:
        csv_writer = csv.writer(new_file,header,lineterminator='\n')
        for line in records:
            if line not in header:
                header.append(sorted(line))
                header.append(sorted(line.values()))
                for x in header:
                    if x not in f:
                        f.append(x)
                        csv_writer.writerow(x)
    return '%s records processed.' % len(records)

# Topic 13: Question 10

# Write a function that reads the /etc/hosts and return the hostname, given the ip address.
def gethostname(ip_address):
    with open('/etc/hosts')as f:
        for i in f :
            i = i.split()
            if i :
                if i[0]== ip_address:
                    return i[1]
    return 'Unknown host'

