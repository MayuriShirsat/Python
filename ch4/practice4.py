# prectice set4
# Que1->program to store seven fruits in a list entered by user
fruits=[]
m1=input("Enter the fruits:")
fruits.append(m1)
m2=input("Enter the fruits:")
fruits.append(m2)
f3=input("Enter the fruits:")
fruits.append(f3)
f4=input("Enter the fruits:")
fruits.append(f4)
m5=input("Enter the fruits:")
fruits.append(m5)
f6=input("Enter the fruits:")
fruits.append(f6)
m7=input("Enter the fruits:")
fruits.append(m7)
print(fruits)

# Que2->program to accept marks of 6 student and display in a sorted manner
marks=[]
m1=int(input("Enter the marks:")) # we have to give input type or it will short as a string ie.,in alphabetical order 
marks.append(m1)
m2=int(input("Enter the marks:"))
marks.append(m2)
m3=int(input("Enter the marks:"))
marks.append(m3)
m4=int(input("Enter the marks:"))
marks.append(m4)
m5=int(input("Enter the marks:"))
marks.append(m5)
m6=int(input("Enter the marks:"))
marks.append(m6)
marks.sort()
print(marks)

# Que3->check that tuple type can not be change in python
a=(12,"mayuri",12.34,455,"hello")
a[2]=54 #TypeError: 'tuple' object does not support item assignment

# Que4->program to sum a list with 4 no.
a=[12,34,2,5]
print(f"summetion is {sum(a)}")

# Que5->program to count no. of zeros in the tuple
a=(7,0,8,0,0,9)
print(f"no of Zeros in this tuple are: {a.count(0)}")
