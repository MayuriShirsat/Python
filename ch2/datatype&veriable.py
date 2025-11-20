#CHAPTER 2->
# Veriable And Datatypes(same as other languages like c,c++)

a=2 #integer
b=1
print(a+b)
name="mayuri" #string
c=2.12 #float 
d= False #boolean
e=None #nothing
#rools to define veriable name->same as c language no special characters are allowed cause they are used by python interpretter internally

# Opperaters in PYTHON->
'''
1)ARITHMATIC
2)ASSIGNMENT
3)COMPARISION
4)LOGICAL

**Keyshortcut->
1)Alt + Click: Hold down the Alt key (Windows/Linux) or Option key (macOS) and click at each desired location to add a cursor.
2)Ctrl + D (Find Next Match): Select a word or phrase, then press Ctrl + D (Windows/Linux) or Cmd + D (macOS) repeatedly to select the next occurrences of that text and add a cursor at each instance.
3)Ctrl + Shift + L (Select All Occurrences): Select a word or phrase, then press Ctrl + Shift + L (Windows/Linux) or Cmd + Shift + L (macOS) to select all occurrences of the selected text in the document and place a cursor at each.
'''

# Typecasting->

f=32 #integer
t=type(f)
print(t)#print the type of a

a="33.3"#string
t=float(a)#typecast in float from string
# similer for int string typecast
x=type(t)
print(x)#print the type of a

# input()function->

a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
# Keyshortcut->Alt+Shift+downarrowkey:to replecate the same line 
print("Number a is:",a)
print("Number b is:",b)
print("A+B:",a+b)

'''Note-> this code do not give the actual addition of two no. 
cause input function take the input in the form of string and if we use "+" operater it perform concatination opration on it not addition
there for it is very imp to specify the datatype of input we are taking'''
