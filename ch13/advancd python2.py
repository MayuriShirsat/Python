# VIRTUAL ENVIROMENT-> 
# in global python enviorment the previous version will lost if we install a new one ie., we can use one version at a time

# So we can make many isolated vertul enviroment in which we can install different python versions in different enviroment and use them as we need
# virtual enviroments are the copies of global enviroment which are isoleted from eachother

# ex., Global python enivroment has Pandas 1.5.2  version
#      And enviroment env1 have Pandas 2.2.2 version

# to activat and use Pandas 2.2.2 we have to create and enter in env1 and install the version using terminal as follow

# pip install virtualenv 
# virtualenv env1(name you want) --> to creat a virtual enviroment
# .\env1\Scripts\activate.ps1 --> to enter(activate) in env1
# pip install pandas --> to install latest version 2.2.2
# import pandas --> to use it

# If we want to use pandas version 1.5.2 we have to exit the env1 by

# deactivate --> to exit env1 
# pip install pandas==1.5.2 --> to install pandas version 1.5.2
# import pandas --> to use


# in this way we can use both versions at a time which is not possibal in Global enviromant as one version lost when new installed

# FREEZE COMMAND-->
# pip freeze->give all the packege present or install in current enviroment

# pip freeze > requirement.txt
# this command write all the packeges into the requirement.txt file

# pip install -r .\requirement.txt 
# by using this command we can recreate exact same copy of the enviroment present in requirement.txt file

# LAMBDA FUNCTION-->
square= lambda x:x*x
print(square(6))
sum= lambda a,b,c:a+b+c
print(sum(1,3,5))

# JOIN METHODE-->
a=["mayuri","sandhya","santosh"]
names="::".join(a)
print(names)

# FORMAT METHOD -->
a= "{1} is a good {0}".format("mayuri","lady")
print(a)
# insted use f-string now

# MAP,FILTER & REDUCE -->
# Map->
l=[1,2,3,4,5]

square= lambda x:x*x
sqlist= map(square,l)
print(list(sqlist))

# Filter->
def even(n):
    if (n%2==0):
        return True
    return False

even_no=filter(even,l)
print(list(even_no))

# Reduce->
from functools import reduce
def sum(a,b):
    return a+b
print(reduce(sum,l))
