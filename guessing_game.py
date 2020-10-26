# You don't need to import random
# to import from random

# import random
from random import randint, choice

# Pre initialization is not required
# in this instance for these specifically.
# Keep them declared in the loop.

# randomNumber = 0
# wrongGuess = 0
# wrongGuess1 = 0

points = 0
lives = 10

# Name
# Inputs dont need to be cast to strings. They
# come that way by default. 
name=input("What is your name?\n")

# Including two examples here for reference:
# These are the two ways to do easier string 
# formatting.

# f-strings (preferred)
print(f"Hello {name} !")

# .format()
# print("Hello {} !".format(name))

while True:
    # Small trick for generating lists is to use
    # something called a "List comprehension".
    # It makes choosing which one is correct a little
    # more difficult but there's another way around it.
    
    # randomNumber = randint(0, 100)
    # wrongGuess = randint(0, 100)
    # wrongGuess1 = randint(0, 100)
    
    numberlist = [randint(0, 100) for _ in range(3)]
    correct = choice(number_list)
    
    random.shuffle(numberlist)

    # Using commas to print numerous variables is
    # fine but not used all that often due to lack
    # of control.
    print(f"{name}, please guess a number from the following list: {numberList}")
    
    answer = int(input())

    # Parentheses not needed (and not recommended
    # unless required by your logic for reasons
    # of precedence.
    if answer != corect:
        print("Wrong, try again!")
        
        # Very basic, not really error handling but
        # "You did wrong, user" code.
        if not answer in numberlist:
            print("Make sure you are choosing a valid number from the list.")
        
        # This is the same as lives = lives - 1
        # but easier shorthand.
        lives -= 1
        
        print(f"Lives remaining: {lives}")
        
        if lives == 0:
            break
        
    else:
        print("Correct!")
        
        # Shorthand for points = points + 1
        points += 1
        print(f"Total points: {points}")

print(f"Thank you for playing the game, {name}.")
