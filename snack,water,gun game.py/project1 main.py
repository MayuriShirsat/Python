# SNACK,WATER,GUN GAME
import random
'''
1 for snack
0 for gun
-1 for water
'''
computer=random.choice(["s","g","w"]) # random.choice take only one argument at a time ex., list tuple etc.,
you=input("Enter s for snack,w for water,and g for gun:")
choiceDict={"s":"snack","w":"water","g":"gun"}

print(f"You choose {choiceDict[you]} and computer choose {choiceDict[computer]}")

if(computer==you):
    print("it's a tie")
else:
    if(computer=="w" and you=="s"):
        print("YOU WIN") 
    elif(computer=="w" and you=="g"):
        print("YOU LOSE") 
    elif(computer=="s" and you=="w"):
        print("YOU LOSE")
    elif(computer=="s" and you=="g"):
        print("YOU WIN")
    elif(computer=="g" and you=="w"):
        print("YOU WIN")
    elif(computer=="g" and you=="s"):
        print("YOU LOSE")
    else:
        print("something want wrong")

