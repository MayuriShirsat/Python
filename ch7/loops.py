# loops->to repeat a set of statement in program
'''Two types of loops in python
1)for loop
2)while loop
'''
# while loop
i=0
while(i<51):
    print(i)
    i+=1 # 1++ is not suported in python

# program to print content of a list
a=[12,"mayuri",43,23.444]
i=0
while(a[i]!=EOFError):
    print(a[i])
    i+=1

# OR
a=[12,"mayuri",43,23.444]
i=0
while(i<len(a)):
    print(a[i])
    i+=1

# for loop
for i in range(1,10):# print from 1 to 1 less then 10 ie., 9
    print(i)

for q in range(12):
    print(q)

for p in range(0,12,2):# from 0 to 12 by jump of 2
    print(p)

# program to print content of a list
l=[1,3,5,7,3,5,7]
for i in l:
    print (i)

# FOR LOOP WITH ELSE->
l=[1,3,5,5,7]
for i in l:
    print (i)
else:
    print("Done") # this is printed when the loop is finished

# BREAK STATEMENT->
for i in range(100):
    if(i==45):
        break # Exit the loop here right now
    print(i)

# CONTINUE STATEMENT->
for i in range(100):
    if(i==45):
        continue # skip this one only
    print(i)

# PASS STATEMENT->is a null statement in python
for i in range(20):
    pass # work on this for loop after some time
# without pass program will through an error
i=0
while(i<10):
    print(i)
    i+=1