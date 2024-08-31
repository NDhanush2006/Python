# Question1. Write a program to read the text from a given file "poem.txt" and find out whether it contains the word "twinkle"

f = open("02_Demo.txt")
c = f.read()
if("twinkle" in c):
    print("The word twinkle is present in the file")

else:
    print("The word twinkle is not present in the file")

f.close()

# Question2.The game() funcrion in a program lets a user play a game and returns the score as an.integer.you need to read a file 'Hi-score.txt' which is eithr blank or contains the previous Hi-score.youu needd to write a program to update the Hi-score whenever the game() function breaks the Hi-score

import random

def game():
    print("Game Starts!, You are Playing")
    score = random.randint(1,62)
    # Fetch Th high score
    with open("02_Demo.txt") as f:
        highscore = f.read()
        if(highscore !=""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your Score:  {score}")
    if(score >highscore or highscore==""):
        with open("02_Demo.txt","w") as f:
            f.write(str(score))

    # Write these score to file
    return  score
    
game()

# Question3.Write a program to generate multiplication table from 2 to 20 and write it  to the different files,place these filess in a folder for a 13-year old
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table+= f"{n} X {i} = {n*i}\n"
    
    #        Folder_name save in /table_files
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)

# Question4.A file contains "Donkey" multiple times. you need to write a program which replace this words with #### by updating same file

word="Donkey"
with open("08_Code.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "Tiger")
with open("08_Code.txt", "w") as f:
     f.write(contentNew)
