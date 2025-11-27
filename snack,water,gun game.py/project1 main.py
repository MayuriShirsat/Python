# SNACK,WATER,GUN GAME->

# import random
# computer=random.choice(["s","g","w"]) # random.choice take only one argument at a time ex., list tuple etc.,
# you=input("Enter s for snack,w for water,and g for gun:")
# choiceDict={"s":"snack","w":"water","g":"gun"}

# print(f"You choose {choiceDict[you]}\nComputer choose {choiceDict[computer]}")

# if(computer==you):
#     print("it's a tie")
# else:
#     if(computer=="w" and you=="s"):
#         print("YOU WIN") 
#     elif(computer=="w" and you=="g"):
#         print("YOU LOSE") 
#     elif(computer=="s" and you=="w"):
#         print("YOU LOSE")
#     elif(computer=="s" and you=="g"):
#         print("YOU WIN")
#     elif(computer=="g" and you=="w"):
#         print("YOU WIN")
#     elif(computer=="g" and you=="s"):
#         print("YOU LOSE")
#     else:
#         print("something want wrong")

# OR

# SNACK,WATER,GUN GAME  (2.0)
import random
# 1 for snack
# 0 for gun
# -1 for water
computer=random.choice([1,-1,0])
youstr=input("Enter s for snack,w for water,and g for gun:")
youdict={"s":1,"g":0,"w":-1}
you=youdict[youstr]
choiceDict={1:"snack",-1:"water",0:"gun"}

print(f"You choose {choiceDict[you]}\nComputer choose {choiceDict[computer]}")

if(computer==you):
    print("It's a tie")
else:
    if((computer - you)== -1 or (computer - you)== 2):
        print("You Lose")
    else:
        print("You Win")   

'''
If we give snake=1 gun=0 and water=(-1) than we will lose when (computer-you) become (-1) or 2 and we win if difference is 1 or (-2)
'''
