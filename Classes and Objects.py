# Topic 10: Question 1
'laptop = Laptop(2000)'

# Topic 10: Question 2
'laptop = Laptop(2000)'
"laptop.change_color('white')"

# Topic 10: Question 3
class Person:
	def __init__(self, weight, height):
		self.weight = weight
		self.height = height

# Create a Person object with weight = 60, height = 1.7
p =Person(weight = 60, height = 1.7)

# Topic 10: Question 4
'def foo(self, bar): '

# Topic 10: Question 5
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.__doc__ = 'A class implementation of a 2-dimensional point.'

    def __str__(self):
        return '(%i, %i)' % (self.x ,self.y)

# Topic 10: Question 6
'Point.x equals to 1 and Point.y equals to 2.'

# Topic 10: Question 7
class Point:
    "A class implementation of 2-Dimensional point."

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
            return   "(%d, %d)" %(self.x + other.x , self.y + other.y)

    def __sub__(self, other):
        return "(%d, %d)"%((self.x - other.x),( self.y - other.y))

# Topic 10: Question 8

class Person:
    """A base class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    """A derived class for Student"""

    def __init__(self, name, age, school):
        self.school = school
        Person.__init__(self, name, age)

    def introduce(self):
       return 'My name is %s. I am %d years old. I am studying at %s.'%( self.name , self.age , self.school)

class WorkingAdult(Person):
    """A derived class for WorkingAdult"""

    def __init__(self, name, age, job):
        self.job = job.lower()
        Person.__init__(self, name, age)

    def introduce(self):
        return 'My name is %s. I am %d years old. I am a %s.'%(self.name, self.age, self.job)

