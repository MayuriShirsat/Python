''' file-> stors(persist) the data permantelly ex., text,mp4(for video),mp3(for songs)

TYPES OF FILE->
1)Text file
2)Binary file
'''
''' code to print working directory(where python find my file.txt)'''

import os
print("Working directory:", os.getcwd())
print("Files inside working directory:", os.listdir())

''' my working directory is "C:\Python" therefore i need to give full path of "file.txt" or following code
->
import os
os.chdir(r"C:\Python\ch9")

with open("file.txt") as f:
    print(f.read()) 
'''
# by "with" file otomatically closed after work

''' 
if my working directory will be "C:\Python\ch9"  
then no full path needed only "file.txt" is sufficient
'''
# TO READ FROM THE FILE->
f=open("C:\\Python\\ch9\\file.txt","r") 
'''
note1->in open() fun the mode is by default "r" so for reading from file it will work even if we not provide mode("r") but for write w have to provide the mode("w")
note2->In Python, backslashes "\" inside strings are escape characters therefore in path we use "\\","/" or row string as ->open(r"C:\Python\ch9\file.txt")
'''
print(f.read())
f.close()

# TO WRITE FROM THE FILE->
st="Hi,I am mayuri"

f=open("myfile.txt","w")
f.write(st)
f.close()

# FILE FUNCTIONS->
f=open("C:\\Python\\ch9\\file.txt")
lines=f.readlines() # read the content of filr line by line
print(lines,type(lines)) # lines print in the form of a list
f.close()

'''redaline() fun read only one line from the file at a time'''

f=open("C:\\Python\\ch9\\file.txt")
# line1=f.readline()
# print(line1)

lines=f.readline()
while(lines!=""):
    print(lines)
    lines=f.readline()
f.close()

# MODES->
"r"
"w"
"a" # open for append
"+" # open for update
"rb" # read in binary
"wb" # write in binary 

st="    Good Morning"

f=open("myfile.txt","a")
f.write(st)
f.close()

# "WITH" STATEMENT->
with open("myfile.txt") as f:
    print(f.read()) # as above
