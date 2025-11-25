# Function-> Group of statement which perform specific task
def avg(): # defination
    a=int(input("Enter a no."))
    b=int(input("Enter a no."))
    c=int(input("Enter a no."))
    average=(a+b+c)/3
    print(average)

avg() # call
avg()

# TYPE OF FUNCTION
'''
1)built in function -> print(),len(),rande()
2)user define function -> define by user
'''
# FUNCTION WITH PARAMETER->
def GoodDay(name,ending):
    print("Good Day,"+name)
    print(ending)

GoodDay("Mayuri","Thank You")

# RETURN->
def GoodDay(name,ending):
    print("Good Day,"+name)
    print(ending)
    return "done" # take this value with itself and give it to the variable which ask 

a=GoodDay("Mayuri","Thank You")
print(a)

# DEFAULT ARGUMENT->
def GoodDay(name,ending="Thanks"):
    print("Good Day,"+name)
    print(ending)

GoodDay("Sandhya")
GoodDay("Mayuri","Thank You")

# RECURSION->fun which call itself
# Que-> find factorial of n
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

n= int(input("Enter any no:"))
print(f"Factorial of the number is:{fact(n)}")
