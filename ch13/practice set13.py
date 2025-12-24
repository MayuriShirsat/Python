# Que1->create two virtual enviroments,install few packeges in the first one. How do you create a similar environment in the 2nd one?

# Ans-->
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# .\env1\Scripts\activate.ps1
# pip install panads
# pip install pyjokes
# pip freeze > requirements.txt
# deactivate
# .\env2\Scripts\activate.ps1
#  pip install -r .\requirements.txt

# Que2->progarm to input name,marks,and phone number of a student and format it using a format function like ->"The name of the student is mayuri , his marks are 90 and phone number is 1234556789"
name=input("Enter your name:")
marks=int(input("Enter your marks:"))
number=int(input("Enter your number:"))

line="The name of the student is {} , his marks are {} and phone number is {}".format(name,marks,number)

print(line)


# Que3->A list contain a table of 7. Write a program to convert it to vertical string of same numbers
table=[str(7*i) for i in range(1,11)]
tb="\n".join(table)
print(tb)

# Que4->write a program to filter a list of numbers which are divisible by 5
li=[12,34,66,55,4,35,58,75]
def divisible5(n):
    if(n%5==0):
        return True
    return False

l=list(filter(divisible5,li))
print(l)

# Que5->program to find the maximum of the numbers in a list using the reduce function
from functools import reduce
l=[12,34,66,55,4,335,58,75]

def greater(a,b):
    if(a>b):
        return a
    return b

# print(reduce(greater,l)) #first check greater between 12 and 34 --> 34 then check greater between 34 and 66-->66 and so on

# Que6->run pip freeze to the system interpreter.Take the content and create a similar virtualenv
# Ans-->
# pip freeze > requirements.txt
# virtualenv ch13env
# .\ch13env\Scripts\Activate.ps1
# pip install -r .\requirements.txt
# deactivate


# Que7->Explore the 'Flask' module and create a web server using Flask & Python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
# Running on http://127.0.0.1:5000 so we have to visit this site to see result (Hello, World!)

# IMPORTANT..............
''' 
Flask makes your Python program act as a server.


http → web protocol
127.0.0.1 → your computer address
5000 → port
/ → path

You created: 
A web server (using Flask) 
A web page at the URL / 
The page sends HTML content to the browser
'''