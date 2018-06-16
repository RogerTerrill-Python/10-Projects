import random

randomNum = random.randint(1,20)
numberGuess = 0
while randomNum != numberGuess:
    numberGuess = int(input("I am thinking of a number between 1 and 20\nTake a guess.\n"))
    if numberGuess > randomNum:
        print("Your number is too high")
        
    elif numberGuess < randomNum:
        print("Your number is too low")
        
print("You found the number!")
