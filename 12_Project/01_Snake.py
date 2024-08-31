'''
Topic :- Project 1 -(Snake ,Watee, gun)


1 for snake
-1 for water
0 for gun

'''
import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice : ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"Snake", -1:"Water", 0 : "Gun"}
you = youDict[youstr]

print(f"You choose : {reverseDict[you]}\nComputer Choose : {reverseDict[computer]}")

if(computer == you):
    print("Yay It's a Draw")

else:
    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("Oppps You Loss")

    elif(computer == 1 and you == -1):
        print("Oppps You Loss")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("Oppps You Loss")

    else:
        print("Something went Wrong")