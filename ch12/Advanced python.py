#1) walrus operator->
# is use to do more then one task in one line 
# ex., assignment and opration on the same variable at the same time
if(n:=len([1,2,3,4,5]) > 3):
    print(f"List is too long ({n} elements, expected <=3)")
# in this we are assiging n = length of list and also comparing it with 3 at the same time rather than doing it in two seperate lines

# 2)Type Defination->
# in this we are defining the type of variable, parameter, return valu for the seek of our understanding 

a : int =12
age : str = "mayuri"

# for function->
def add(a:int,b:int) -> int:
    return a+b
print(add(12,13))

# 3) Type hint-> do the same as above but for list,tuple,dict etc

from typing import List,Tuple,Dict,Union

# list of integers
numbers: List[int] = [1,2,5,3,6]
# Tuple of a string and a integer
person: Tuple[str,int] = ["dwd",12]
# dictionary with string key and integer value
score: Dict[str,int] = {"mayuri":21,"sanddy":30}
# Unoin that can hold multiple types
id: Union[int,str] = "ID1234"
# or
id=1234

# 4)Match case->samr as switch cases in c,c++
def check_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "NOT FOUND"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
print(check_status(5007))

# 5)merge Dictionary
dic1={'a':1,'b':3}
dic2={'a':1,'c':3}
merged= dic1 | dic2
print(merged) # print without repetation


# Exception Handling in Python->
# use to avoide the program crash due to error if and error accure at the middle of program then the reamining program will do not run to avoid this we externally give a error handing statement so that even if erroe accour the program run as it is

try:
    a=int(input("Enter a number:"))
    print(a)

except Exception as e:
    print("value error")
    print(e) 

else:
    print("you entered a valide no") # peongram enter in else only if the try block is true

finally:
    print("I am Inside the finally") # this block of code run in try and  in except also (in any condition)
    # this block is usefull in function. Even if we return something in a fun the finally block run

print("Thank you") # this code run in try and except also 
print("Good Day")
# this code run same as finally block but when in a function we return something this code dose not run


# Reising Exception -> We can raise custom exceptions using the 'rise' keyword in python

a= int(input("Enter a number:"))
b= int(input("Enter 2nd number:"))

if(b==0):
    raise ZeroDivisionError("Heyy our program is not suppouse to divide by zero")
else:
    print(f"The Division is: {a/b}")

print("Have a good Day") # if division error occure then this code do not run

# some time if the error is more critical than we have to rise it and crash the program so that the user know about it and currect it


# __name__ --> gives the file name (current file or imported file name) from where the executed code belongs

from module import myfun # output-> module (imported file name)
# see module.py file
# the code inside if in imported file (module.py) do not run here

# output will be 1)__main__ -->for current file
#                2)filename -->if we are using the module in current program

# Global keyword-> change the value of golbal variable

a=12
def fun():
    global a
    a=3 # golbal variable change from 12 to 3
    print(a) # output-> 3

fun()
print(a)  # output-> 3

# Enumerete function-->
l=[1,34,3,43,465]

index=0
for item in l:
    print(f"The item at index {index} is {item}")
    index+=1

# we can do the same by Enumerate function as follow
for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")

# List comprehensions->
mylist=[1,34,3,43,465]

# to sqare the items in mylist
sqaredlist = [i*i for i in mylist]
print(sqaredlist)