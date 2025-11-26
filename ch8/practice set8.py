# Que1->program to find gra=eater of three no.
def greater(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greater")
    if(b>a and b>c):
        print(f"{b} is greater")
    if(c>b and c>a):
        print(f"{c} is greater")

p=int(input("Enter 1st no:"))
q=int(input("Enter 2nd no:"))
r=int(input("Enter 3rd no:"))
greater(p,q,r)

# Que2->program to conver Celsius to Fahrenheit
def fahtocel(f):
    return 5*((f-32)/9)

a=int(input("Enter the temperature in fahrenheit:"))
print(f"temperature in celcius is:{round(fahtocel(a),2)} °C")

# (window key + .) for emoji pannel

# Que3->how to prevent a python print() fun to print a mew line at the end
print("Enter",end="") 
print("hi") # python atomatically add new line after every print fun end prevent this

# Que4->recursive fun to calculate sum of first n natural no.
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

a=int(input(f"Enter a value:"))
print(f"sumation is:{sum(a)}")

# Que5->print pattern
'''
***
**
*
'''
def pattern(n):
    if(n==0):
        return # end this fun here
    print("*"*n)
    pattern(n-1)

pattern(5)
print("")

# Que6->fun to convert inches to cms
def intocm(i):
    return i*2.54

a=int(input(f"Enter a value in inches:"))
print(f"Value in cms:{intocm(a)}")

# Que7->program to print table of given no.
def table(n):
    for i in range(1,11):
        print(f"{n}X{i} = {n*i}")

a=int(input("Enter tne no you want:"))
table(a)