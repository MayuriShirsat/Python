# Que1->create a class "programmer" for storing information of few programmers working at Microsoft
class programmer:
    company="Microsoft"

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        
mayuri=programmer("mayuri",720000,"Python")
santosh=programmer("santosh",700000,"java")
print(mayuri.company,mayuri.name,mayuri.salary)
print(santosh.name,santosh.salary)

# Que2->a class "Calculator" capable of finding square,cube and squareroot of a no.
class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"sqaur is:{self.n*self.n}")
    def cube(self):
        print(f"cube is:{self.n*self.n*self.n}")
    def squareroot(self):
        print(f"squareroot is:{self.n**0.5}")

obj=calculator(16)
obj.square()
obj.cube()
obj.squareroot()

# Que3->create a class with a attribute "a" (say name) ;create a obj attribute  a=0. Dose this change the class attribute?
class demo:
    a=34

obj=demo()
print(obj.a)
obj.a=0
print(obj.a)

print(demo.a)

# This do not change class attribute but first preference is of obj attribute

# Que4->add a static method in problem 2 to greet the user with "hello"
class calculator:
    def __init__(self,n):
        self.n=n
    @staticmethod
    def greet():
        print("Hello")
    def square(self):
        print(f"sqaur is:{self.n*self.n}")
    def cube(self):
        print(f"cube is:{self.n*self.n*self.n}")
    def squareroot(self):
        print(f"squareroot is:{self.n**0.5}")

obj=calculator(16)
obj.greet()
obj.square()
obj.cube()
obj.squareroot()

# Que5->create a class train which has meh=thods to book a tickit,get status and get payment for tickit 
 
from random import randint # use of from keyward
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in train no:{self.trainNo} from {fro} to {to}")
    def getstatus(self):
        print(f"Train no:{self.trainNo} is running on time")
    def pay(self,fro,to):
        print(f"payment for Tickit of Train no:{self.trainNo} from {fro} to {to} is {randint(10,5000)}")

t=Train(12334)
t.book("pune","Bangluru")
t.getstatus()
t.pay("pune","Bangluru")

# Que6->can you changr the self parameter inside a class to something else.
class demo:
    def sum(sf,a,b):
        print(f"summation is:{a + b}")

obj=demo()
obj.sum(4,6)
# it is possible to use other word but it must be the first parameter of every instance method.