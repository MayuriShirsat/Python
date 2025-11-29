# inheritance->one class can take(inherit) porpertise of another class

class coder: # base class
    language="python"
    def coding(self):
        print(f"You are a good coder")

class Employee: # base class
    company="ITC"
    def show(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"The name of the Employee is {self.name} and salary is {self.salary}")
    
class programmer(Employee,coder): # derived class
    def showlang(self):
        print(f"The name of company is {self.company} and he is good in {self.language} language")


a=Employee()
p=programmer()
c=coder()

print(a.company,p.company)
a.show("santosh",700000)
p.show("sandhya",400000)
p.coding()
p.showlang()

'''
TYPES OF INHERITANCE->
1)single -> one derived class from one base class
2)multiple ->one derived class from multiple derived classes
3)multilevel -> deriving class from derived class
'''
class aa:
    a=1
class bb(aa):
    b=2
class cc(bb):
    c=3

x=aa()
y=bb()
z=cc()
print(x.a)
# print(x.b) # give error
print(y.a,y.b)
# print(y.c) # give error
print(z.a,z.b,z.c)

# SUPER() METHODE->is use to call the constructor of super class when constructor of derived class is called
class aa:
    def __init__(self):
        print("constructor of base class")
    a=1
class bb(aa):
    def __init__(self):
        super().__init__() # call constructor of parent class
        print("constructor of derived class")
    b=2

y=bb()

# CLASS METHODES->this give the value of class attribute even though the obj attribute have the preference
class aa:
    a=1
    @classmethod # decoretor
    def show(cls):
        print(f"The value of class attribute a is:{cls.a}")

x=aa()
x.a=23
x.show() # this do not print '23' as classmethod decoretor is used it print '1'

# PROPERTY DECORETORS->
class employee:

    @property # let user use name as a variable but treated as a fun internally
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        parts=value.split(" ") # splite the value from the spacs(" ") is present and form a list of 2 values {"Mayuri","Shirsat"}
        self.fname=parts[0]
        self.lname=parts[1]

e=employee()
e.name="Mayuri Shirsat" # setter run here value="Mayuri Shirsat" it split it in ["mayuri","shirsat"]
print(e.name) # getter(property) run here

'''
in this program abstraction is done as user is not entering first name and last name seperatlly user enter full name but internall it is splitting into fname and lname user dont konw that spliting of name is done inside as it get it's full name at output
'''
# Operator Overloading = You define new behaviour for old operators like(+,-,*,ets.,)
'''
Giving special meaning to operators like +, -, <, >, ==, * when they are used with objects of your own class.

Python already knows how to add
2 + 3 → numbers
"a" + "b" → strings

But if you try:
p1 + p2
where p1 and p2 are objects of your class,
Python does NOT know how to add them.
So you define it using magic(dunder) methods.
'''
class number:
    def __init__(self,n):
        self.n=n

    def __add__(self,other): # here self = 2 and other = 23
        return self.n + other.n
    
a=number(2)
b=number(23)

print(a+b) # summetion of obj

# Operators like + are actually functions internally.
# Example: a + b
# is actually: a.__add__(b)
# So we override these methods to decide what + means for our objects.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overload str() for printing
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2   # calls __add__
print(p3)      # calls __str__