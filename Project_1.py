## Guess a random number

import random

target = random.randint(1,100)

while True:
    userchoice = input("Guess the target or Quit :")
    if (userchoice == "Quit"):
        break
    
    userchoice = int(userchoice)
    if(userchoice == target):
        print("Success: CorrectGuess!!")
    elif(userchoice < target):
        print("your guess was too small. Take a bigger guess...")
    else:
        print("your guess was too big . Take a small guess...")
    
print("-----GAME OVER------")    
    
