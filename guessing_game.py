import random
from random import randint


# Initial numbers

randomNumber = 0
wrongGuess = 0
wrongGuess1 = 0

points = 0

lives = 10


# Name
name=str(input("What is your name?\n"))
print("Hello",name +"!\n")

while True:
    randomNumber = randint(0, 100)
    wrongGuess = randint(0, 100)
    wrongGuess1 = randint(0, 100)
    
    numberlist = [randomNumber, wrongGuess, wrongGuess1]
    random.shuffle(numberlist)

    print(name + ", please guess a number from the following list.\n", numberlist)
    answer=int(input())

    if (answer != randomNumber):
        print("Wrong, try again!")
        lives = lives - 1
        print("Lives remainin: " + str(lives)+"\n")
        if lives == 0:
            break
        
    else:
        print("Correct!")
        points = points + 1
        print("Total points: " + str(points) + "\n")

print("Thank you for playing the game,", name + ".")