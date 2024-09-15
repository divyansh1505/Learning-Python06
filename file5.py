# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the 
# Hiscore whenever the game() function breaks the Hi-score

import random 

def game():
    print("You are playing the game.....")
    score = random.randint(1,5000)
    #it randomly chooses a number in the given range
    with open("hiscore.txt") as g:
        hiscore = g.read()
    if (hiscore!= ""):
        hiscore = int(hiscore)   #mtlb agar khali nhi tha, to jo tha usko int me convert krlia
    else : 
        hiscore = 0 
    print(f"Your score : {score}")
    if (score > hiscore):
        with open("hiscore.txt", "w") as g:
           g.write(str(score))  #as score was int so we converted to string
           print("NEW HIGH SCORE BITCH")
    
    return score

game()