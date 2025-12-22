# Que1->write a program to open three files 1.txt, 2.txt, 3.txt id any these files are not present ,a message without exiting tr program must be printed prompting the same

try:
    with open ("ch12//1.txt","r") as f:
        print(f.read())
        print("1.txt is opened")
except Exception as e:
    print(e)

try:
    with open ("ch12//2.txt","r"):
        print("2.txt is opened")
except Exception as e:
    print(e)

try:
    with open ("ch12//3.txt","r"):
        print("3.txt is opened")
except Exception as e:
    print(e)

# Que2-> write a program to print 3re, 5th, and 7th element from a list using enumerate function

lis=[23,3,7,23,57,3434,1,45,67]

for index,element in enumerate(lis):
    if(index>3 & index<9 & index%2 != 0):
        print(f"{index}:{element}")
        index+=1

# Que3-> print a table of no enterd by user using list comprahentions
a= int(input("Enter a number:"))

table=[a*i for i in range(1,11)]
print(table)

# Que4->program to display a/b. If b=0 then display infinite by handling 'ZeroDivision Error'
try:
    a= int(input("Enter a number:"))
    b= int(input("Enter 2nd number:"))
    print(f"The Division is: {a/b}")
except ZeroDivisionError as v:
    print("Infinite")

# Que5->stored the table in que 3 in file named as Table.txt
a= int(input("Enter a number:"))

table=[a*i for i in range(1,11)]

with open("Table.txt","w") as f:
    f.write(f"table of {a}:{str(table)} \n")