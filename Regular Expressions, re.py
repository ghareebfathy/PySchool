# Topic 12: Question 1
# Fill in the appropriate 'pattern' and 'string' pareameters for 'findall' in following exercises.
import re
a = re.findall(  'e'    , 'pareameters')  # len(a) = 3
b = re.findall( 'a',        'aaaa'     )  # len(b) = 4

# Topic 12: Question 2
a = ['ne']
b = ['c']

# Topic 12: Question 3
a = ['aeroplane']
b = ['aeroplane']
c = ['ae', 'ro', 'pl', 'an', 'e']

# Topic 12: Question 4
# Replace the m,n in the regular expressions below so that they
# matches the descriptions to the right.
import re
regex_1 = 'b{3}'     #  match exactly 4 characters
regex_2 = '{0,4}'   #  match 0 or more characters
regex_3 = '{0,1}'   #  match 0 or 1 character
regex_4 = '{4}'   #  match 1 or more character

# Topic 12: Question 5
# Complete the character sets in the regualar expressions below so that they
# matches the descriptions to the right.
import re
regex_1 = '[a,b,d]'     #  match a to z
regex_2 = '[C,F,H]'     #  match A to Z
regex_3 = '[1,a,2,B,0]'     #  match alphanumeric characters

# Topic 12: Question 6

# Initialize the variables "regex" and "target" which produces the output in the example above.
import re
regex  ="com|edu|org"
target="orgeducom"

# Topic 12: Question 7
"'\d+' is equivalent to '[0-9+]'. "

# Topic 12: Question 8
# Write down the equivalent RE for \w and \W using character set [ ].
import re
regex_1 =  '[\w]'  # \w
regex_2 =  '[\W]'  # \W

# Topic 12: Question 9

# Complete the RE below to match the output of the above example.
import re
regex = r'([9-z])([0-z])\2'

# Topic 12: Question 10
# Complete the RE below to match the output of the above examples.
# The RE should be as generic as possible.
import re
regex1 = r"([\d]{2})[^2]([\w]{3})"
regex2 = r"(\w)\d{3}(\w)"

# Topic 12: Question 11

# Complete the RE below to match the output of the above examples.
# Hint 1: Match 1 to 3 letters, followed by at least 1 decimal digit.
import re
regex = r'[a-z]{0,9}[\d]+\d'

# Topic 12: Question 12

# Fill in arbitrary value to the string so that mobj.span(2) returns (5, 7).
import re
mobj = re.search('(\d+)/(\d+)', 'pi=9/12, compute ...')

# Topic 12: Question 13
# Fill in the RE below so that the resulting string will remove double vowel with single
# vowel.
import re
regex =r'([a-z])\1+'
repl = r'\1'

# Topic 12: Question 14

import re
def validate(passwd):
    if len(passwd)>= 6 and len(passwd)== 8 and   re.search(r'\d[9-z][^a-z]',passwd):
        return 'Valid password.'
    else:
        return  'Invalid password.'

# Topic 12: Question 15
import re
def validate(email):
    if re.match(r'^[a-zA-Z0-9.]+@.+(com|edu|org)$', email):

        return  'Valid email.'
    else:
        return   'Invalid email.'

