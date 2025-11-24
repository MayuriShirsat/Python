# practice set6
# Que1->porgram to find greatest of 4 no. entred by the user
a1=int(input("Enter the no."))
a2=int(input("Enter the no."))
a3=int(input("Enter the no."))
a4=int(input("Enter the no."))
if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest no is:",a1)
if(a2>a1 and a2>a3 and a2>a4):
    print("Greatest no is:",a2)
if(a3>a2 and a3>a1 and a3>a4):
    print("Greatest no is:",a3)
if(a4>a2 and a4>a3 and a4>a1):
    print("Greatest no is:",a4)

# Que2->program to find a student is pass or failed if it requires a total of 40% and at least 33% in each subject ot pass. assume 3 subjects and take marks as input from the user
maths=int(input("Enter the marks of Maths out of 100:"))
Eng=int(input("Enter the marks of English out of 100:"))
Hin=int(input("Enter the marks of Hindi out of 100:"))
if(maths>100 or Eng>100 or Hin>100):
    print("Please enter valid marks")
elif(((maths+Eng+Hin)/3)>=40 and maths>=33 and Eng>=33 and Hin>=33):
    print("Congratulation you are passed!",(maths+Eng+Hin)/3)
else:
    print("Sorry! Better luck next time")

# Que3->a spam comment is defined as a text aontaining following keywords:"Make a lot of money","buy now","subscribe this","click this".write a program to detect these spam
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
m=input("Enter your Message:")
if(p1 in m or p2 in m or p3 in m or p4 in m):
    print("Alert!!!! This is a Spam")
else:
    print("This isn't a Spam you are safe to go on")

# Que4->program to find weather the given username contain less than 10 characters or not
name=input("Enter username here:")
if(len(name)<=10):
    print("Username contain less than 10 characters")
else:
    print("characters in username are greater than 10")

# Que5->program which find out given name is present in a list or not
username=["mayuri","sandhya","simran","khushi"]
name=input("Enter username here:")
if(name in username):
    print("Username already exist")
else:
    print("Username is not exist")

# Que6->
marks=int(input("Enter the marks out of 100:"))
if(marks>=90 and marks<=100):
    print("congratulations! you are pass with grade Ex")
elif(marks>=80 and marks<=90):
    print("congratulations! you are pass with grade A")
elif(marks>=70 and marks<=80):
    print("congratulations! you are pass with grade B")
elif(marks>=60 and marks<=70):
    print("congratulations! you are pass with grade C")
elif(marks>=50 and marks<=60):
    print("congratulations! you are pass with grade D")
else:
    print("sorry you are Fail")

# Que7->program to find whether given post is talking about Mayuri or not
post=input("Enter the post here:")
if("Mayuri" in post or "mayuri" in post):
    print("Post is about Mayuri")
else:
    print("Post is not about Mayuri")
