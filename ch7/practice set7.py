# practide set7
# Que1->program to print a table of given no.
a=int(input("Enter no:"))
for i in range(1,11):
    print(f"{a}X{i}={a*i}")
# OR
i=1
while(i<=10):
    print(a*i)
    i+=1

# Que2->program to greet all the preson names stored in l and start with "s"
l={"Santosh","Mayuri","sandhya","Omkar","Swati"}
for i in l:
    if(i.startswith("S")):
        print(f"Hello {i} Good Morning")

# Que3-> program to find whether the given no. is prime or not
a=int(input("Enter any no."))
for i in range(2,a):
    if(a%i==0):
        print("It is not a Prime no.")
        break
else:
    print("It is a Prime no.")   

# Que4->pragram to find the sum of 1st n natural no.s using while loop
a=int(input("Enter any no."))
i=1
tottle=0
while(i<=a):
    tottle=tottle+i
    i+=1
print(f"sum is:{tottle}")

# Que5->progran to cLCULte factorial of given no.
a=int(input("Enter any no:"))
i=1
fact=1
while(i<=a):
    fact=fact*i
    i+=1
print(f"factorial is:{fact}")
# OR
a=int(input("Enter any no:"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(f"factorial is:{fact}")

# Que6->write the program for the following star pattern 
'''
  *
 ***
***** for n=3
'''
# print("  *\n ***\n*****") # as simple as making noodles just kidding its not the perfact way

a=int(input("Enter any no:"))
for i in range(1,a+1): # for no of lines
    print(" "* (a-i),end="")   # for space
    print("*"* ((2*i)-1),end="") #for "*"
    print("") # for next line

'''
Print the stars "*" * ((2*i)-1)
After printing, add nothing (no newline, no space)
withodu end"" the spaces and stars are not printed on the same line
  
*

 
***


*****
'''

# Que7->print 
'''
*
**
***
'''
a=int(input("Enter any no:"))
for i in range(1,a+1): # for no of lines
    print(" "* (a-i),end="")   # for space
    print("*"*i,end="") #for "*" end"" mean do not add anything no newline no space nothing
    print("") # for next line

# Que8->print
'''
*****
*   *
*   *
*   *
*****
'''
a=int(input("Enter any no:"))
for i in range(1,a+1): 
    if(i==1 or i==a):
        print("*"*a, end="")     
    else:
        print("*", end="")
        print(" "*(a-2), end="")
        print("*", end="")
    print("")

# Que9->program to print a table in reverse order of given no.
a=int(input("Enter no:"))
for i in range(10,0,-1):
    print(f"{a}X{i}={a*i}")
# OR
a=int(input("Enter no:"))
for i in range(1,11):
    print(f"{a}X{11-i}={a*(11-i)}")