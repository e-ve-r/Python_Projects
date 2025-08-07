import random

print("Welcome to the Higher Lower game!\n")

level = input("choose a level of difficulty, type 'easy' or 'hard' to start\n")
random_number = random.randint(1, 100)

if (level == "easy"):
    chances = 10
else:
    chances = 5

while chances > 0:
    picked_number = int(input("Please guess a number between 1 and 100\n"))

    if picked_number > random_number:
        chances -= 1
        print("Too high, you have", chances, "chances left")
    elif picked_number < random_number:
        chances -= 1
        print("Too low  , you have", chances, "chances left")
    else:
        if level == "easy":
            print("You guessed it right! in ", 11 - chances, "tries")
        else:
            print("You guessed it right! in ", 6 - chances, "tries")
        break


