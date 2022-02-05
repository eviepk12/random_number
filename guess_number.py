# Small guess the number game in python
# made my enal

import random

def guessNumber(x):
    randomNumber = random.randint(1, x)
    guess = 0 #declared 0 so the number never goes below 1

    while guess != randomNumber: 
        guess = int(input(f"Guess a number between 1 and 10 : " ))

        if guess < randomNumber:
            print("Sorry, you guessed too low!")
        elif guess > randomNumber:
            print("Sorry, you guessed too high!")
        
    print(f"Yay!!!, you guessed the number {randomNumber} correctly!!")

def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    
    while feedback != "c":
        if low != high: 
            guess = random.randint(low, high)
        else:
            guess = low
        
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)??? : ").lower() # because we had "c" in lower cases, having the user input in upper case would not work. So .lower is converting the input to lowercases
        if feedback == "h":
            high = guess - 1 
        elif feedback == "l":
            low = guess + 1

    print(f"Yay!!! The computer correctly guessed your number, {guess}, the computer uprising will begin soon!!!!!")


print("Choose which one you would like to play")
print("1. Guess a number the computer have selected randomly")
print("2. Computer Guess (think of a number and the nunmber will guess it)")
print("----------------------------------------------")

option = int(input("Type the option you want : "))

match option: 
    case 1:
        guessNumber(int(input("How much of the range do you want the number to be? : ")))
    case 2:
        computerGuess(int(input("Think of a number, and How much of the range do you want the number to be? : ")))
    case _:
        print("Choose the correct option!!")