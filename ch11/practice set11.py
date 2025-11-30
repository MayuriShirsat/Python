# QUE1->create a class (2=D vector) and use it to create another class represanting q 3-D vector
class vector2_D:
    def __init__(self,p,r):
        self.p=p
        self.r=r
    def show(self):
        print(f"thre vectoe is  {self.p}p + {self.r}r")    

class vector3_D(vector2_D):
    def __init__(self,p,r,k):
        super().__init__(p,r)
        self.k=k
    def show(self):
        print(f"thre vectoe is {self.p}p + {self.r}r + {self.k}k")    

a=vector2_D(1,2)
b=vector3_D(3,2,6)
a.show()
b.show()

# Que2->create a class "pets" from a class "animals" and futher create a class "dog" from "pets" add a method "bark" to class "dog"
class Animals:
    @staticmethod
    def showAnimal():
        print("I am a Animal")

class Pets(Animals):
    @staticmethod
    def showPet():
        print("I am a pet")

class Dog(Pets):
    print("I am a Dog")
    @staticmethod
    def bark():
        print("I can bark")
        
d=Dog()
d.bark()
d.showAnimal()

# Que3->create a class "Employee" and add salary and increment properties to it write a method 'saalryAfterIncrement' with a @property decoretor with a setter which change the value of increment based on salary

class Employee:
    salary=720000
    increment=20
    insalary=salary + (salary*(increment/100))
    @property
    def salaryAfterIncrement(self):
        return (f"salary After Increment is :{self.insalary}")  

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        # new salary = old salary(1+increment/100)
        # increment= ((new salary/old salary)-1)*100
            self.increment=((self.insalary/self.salary)-1)*100

e=Employee()
print(e.salaryAfterIncrement)

e.salaryAfterIncrement=792000.0
# setter runs only when you assign a value as :e.salaryAfterIncrement = 30000  
print(e.increment)

# Que4-> write a class "complex" to reperesent complex no. along with overloaded operetor "+" and "*" which adds and multiplies them
class complex:
    def __init__(self,p,r):
        self.p=p
        self.r=r

    def __add__(self,other):
        return complex(self.p + other.p ,self.r + other.r)
        ''' if i only print anything inside dunder fun and not return something then this will happen->
            Operator overloading functions (__add__ and __mul__) must return a new object, not just print values.
            Because you only print inside the method but do not return anything, Python returns None.
            That's why print(c1 + c2) gives:    3 4
                                            None
        '''
    def __mul__(self,other):
        # (a+bi)(c+di) = (ac - bd) + (ad + bc)i
        real = (self.p * other.p) - (self.r * other.r)
        imag = (self.p * other.r) + (self.r * other.p)
        return complex(real, imag)
        
    def __str__(self):
        return f"{self.p} + {self.r}i"
    # Without __str__, Python prints: <__main__.complex object at 0x...>

c1=complex(1,2)
c2=complex(2,2)
print(c1+c2)
print(c1*c2)

# Que5->write a class "Vector" representing a vector of n dimensions.Overload the '+' and '*' operators which calculate the sum and dot(.) product of them 
# Que6->write a __str__() methode to print the vector as follow=-> 2i+9j+7k
class Vector:
    def __init__(self,p,q,r):
        self.p=p
        self.q=q
        self.r=r

    def __add__(self,other):
        return Vector(self.p + other.p ,self.q + other.q,self.r + other.r)
    
    def __mul__(self,other):
        return Vector(self.p * other.p ,self.q * other.q,self.r * other.r)

        
    def __str__(self):
        return f"Vector=({self.p}i+{self.q}j+{self.r}k)"

c1=Vector(1,2,3)
c2=Vector(2,2,5)
print(c1+c2)
print(c1*c2)

# Que7-> Override the __len__() method on vector of problem 5 
class Vector:
    def __init__(self,list):
        self.list=list
    
    def __len__(self):
        return len(self.list)

c1=Vector([1,2,3])
print(len(c1))
