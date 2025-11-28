# Que1->read the text from the 'poem.txt' and find whether it contain the word 'twinkel'
with open("poem.txt","r")as f:
    contain= f.read()
    if("twinkle" in contain.lower()):
        print("Twinkel is present in file")
    else:
        print("Twinkle is not present in file")    

# Que2->game()fun in a program lets a user play a game and returns the score as an integer. You need read a file "Hi-score.txt" which is either blank or contain the privious hiscore. You need to write a program to update the hi-score whenever the game() fun break the hi-score
import random
def game():
    print("Starting the game......")
    score=random.randint(1,100)

    with open("hi-score.txt","r") as f:
        hiscore=f.read()
        if(hiscore != ""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"Your score is:{score}")

    if(score>hiscore):
        print("🎉🎉New High Score")
        with open("hi-score.txt","w") as f:
            f.write(str(score))
    return score            

game()

# Que3->program to generate tables from 2 to 20 amad write it to the different files. Place these files in a folder
def table(n):
    table=""
    for i in range(1,11):
        table+= f"{n}X{i} = {n*i}\n"

    with open(f"tables2to20/table{n}.txt","w") as f:
        f.write(table)

for a in range(2,21):
    table(a)

# Que4-> a file a word "donkey" many times. you need to write a program which replace word with #### by updating the same file
with open("donkey.txt","r") as f:
    content=f.read().lower()

    new=content.replace("donkey","####")

with open("donkey.txt","w") as f:
    f.write(new)

# Que5->repeat problem 4 for a list of such words to be censored
words=["donkey","python","nice"]

with open("donkey.txt","r") as f:
    content=f.read().lower()

for word in words:
        new=content.replace(word,"#"*len(word))

with open("donkey.txt","w") as f:
    f.write(new)

# Que6->write a program to a log file and find out whether it contain "python" and write line no where it is present
with open("file.html","r") as f:
    lines=f.readlines()

    lineno=1
for line in lines:
        if("python" in line.lower()):
            print(f"\"python\" is present at line no:{lineno}")
            break
        lineno+=1
else:
      print("NO \"python\" is not present")

# Que7->make a copy of a text file "this..txt"
with open("file.html","r") as f:
    content=f.read()
with open("this.txt","w") as f:
    f.write(content)    

# Que8->program to find out where a file is identical to other file or not
with open("file.html","r") as f:
    content=f.read()
with open("poem.txt","r") as f:
    data=f.read()

if(content==data):
    print("files are identical")
else:
    print("file are not identical") 

# Que9->program to wipe out a file 
with open("this.txt","w") as f:
    f.write(" ")    

# Que10->rename a file to "renamed_by_python.txt"
import os
old_name = "oldfile.txt"
new_name = "renamed_by_python.txt"

os.rename(old_name, new_name)
print("File renamed successfully!")

# this program will through an error now as the program is run successfully once the file "oldfile.txt" is renamed as "renamed_by_python.txt" therefor there is no file named "oldfile.txt" in present folder to run this program 2nd time