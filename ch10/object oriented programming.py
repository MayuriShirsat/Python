'''TWO OPPORACHES OF PROGRAMING->
1)OOPs APPROACH->solving a program by creating object
2)FUNCTIONAL APPROACH->
'''
'''
CLASS->blueprint for creating object
for example-> a blank form do not contain information about any student.But if a certain student say "rahul" fill the form then the form is  "application of rahul" same if it is filled by "manjiri" then it is "application of manjiri"

here the blank form is same as CLASS and if someone filled the form then it is same as OBJECT 

'''
class  employee:
    name="Mayuri"
    language="C,C++,Python" # this is an class attribute
    salary=420000


obj=employee
print(obj.name,obj.language,obj.salary) 
rohan=employee()
rohan.name="rohan rahul khan" # obj attribute have high preference than that of class attribute here "rohan-----" will print in attribute insted of "mayuri"
rohan.deparment="HR" # this is an obj attribute
print(rohan.name,rohan.language,rohan.salary,rohan.deparment)


''' 
 here deparement is object attribute(instance attributes) and name,salary are class attribute

 when class is defined only a template(info) is defined .Memory is allocated only after object instantiation

 object can invoke the methodes available without revealing the implementation details to the user-ABSTRACTIONS & INCAPSULATION
 '''

#  SELF PARAMETER->when we define any fun(method) inside a class than it require a parameter to pass in it whenever we want to call the fun

# class  employee:
#     name="Mayuri"
#     salary=420000
#     def getInfo():
#         print(f"Tha name is {name} andthe salary is {salary}.")

# mayuri=employee()
# mayuri.getInfo()


# this code will through an error cause when we call obj.getInfo()  it is same as employee.getInfo(mayuri) there for we are passing an argument but in fun defination we have no parameter given

# RIGHT CODE->
class  employee:
    name="Mayuri"
    salary=420000
    def getInfo(self):
        print(f"The name is: {self.name} and the salary is:{self.salary}.")

mayuri=employee()
mayuri.getInfo() # employee.getInfo(mayuri)


# we can use anything insted of "self" like "a","cr",etc.,
# STATIC METHOD->if the method is not using any attributes ex., "self.name" then there is no need to pass any parameter oe obj this is done by static methodes

class  employee:
    name="Mayuri"
    salary=420000

    def getInfo(self):
        print(f"The name is: {self.name} and the salary is:{self.salary}.")

    @staticmethod
    def greet():
        print("Good Morinng") # not using any attribute    

mayuri=employee()
mayuri.greet()
mayuri.getInfo() # employee.getInfo(mayuri)


# __init__() CONSTRUCTOR->call atomatically whenever method is called
class  employee:
    name="Mayuri"
    salary=420000

    def __init__(cl,name,salary,lang): # dunder methode -> methode start with "__" 
        print("I am A constructor")
        cl.name=name
        cl.salary=salary
        cl.lang=lang

    def getInfo(self):
        print(f"The name is: {self.name} and the salary is:{self.salary}.")

sandhya=employee("sandhya",420000,"All") # dunder methode is called atomatically
sandhya.getInfo()
print(sandhya.name,sandhya.salary)

