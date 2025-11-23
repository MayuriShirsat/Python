# practice set5->
# Que1->program to create a dictionary of hind words with values as their English transaction.Provide user with an option to look it up!
dictinary={
    "madad":"help",
    "sunder":"beautifull",
    "billi":"cat",
    "plang":"bed"
}
word=input("Enter the world you want the meaning of:")
print(dictinary[word])

# Que2->program to input 8 no. from the user and display all the unnique no.
p=set()
m1=int(input("Enter the no:")) 
p.add(m1)
m2=int(input("Enter the no:"))
p.add(m2)
m3=int(input("Enter the no:"))
p.add(m3)
m4=int(input("Enter the no:"))
p.add(m4)
m5=int(input("Enter the no:"))
p.add(m5)
m6=int(input("Enter the no:"))
p.add(m6)
m7=int(input("Enter the no:"))
p.add(m7)
m8=int(input("Enter the no:"))
p.add(m8)
print(p)

# Que3->check can we have 18(int)and 18(str) as a value in it
p={18,'18'}
print(p,type(p))

# Que4->what will be the length of following set
s=set()
s.add(18)
s.add('18')
s.add(18.0) #in python 1==1.0 cause it is numerically equal
print(len(s)) #it will bw 2 not 3


# Que5->create an empty dictionary.Allow 4 frinds to enter there favorite language as values and use their names as ke)nt(input("Enter the language you like:")) # we have to give input type or it will short as a string ie.,in alphabetical orde)
d={}
lang=(input("Enter your name:"))
name=(input("Enter the language you like:"))
d.update({name:lang})
lang=(input("Enter your name:"))
name=(input("Enter the language you like:"))
d.update({name:lang})
lang=(input("Enter your name:"))
name=(input("Enter the language you like:"))
d.update({name:lang})
lang=(input("Enter your name:"))
name=(input("Enter the language you like:"))
d.update({name:lang})
print(d)
# If 2 frinds have same name but different languages then python assign the 2nd entred language to the first name at the place of 1st language
 