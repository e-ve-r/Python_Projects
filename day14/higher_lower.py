import random
import game_data
import icons

A = {}
B = {}
Score = 0

def random_option_A():
    global A
    A = random.choice(game_data.data)
    return A

def random_option_B():
    global B, A
    B = random.choice(game_data.data)
    while A == B:
        B = random.choice(game_data.data)
    return B

A = random_option_A()
B = random_option_B()

while True:
    print(" "*100)
    print(icons.welcome_message)
    print(f"{A['name']}, from {A['country']}, is a {A['description']}")
    print(icons.vs)
    print(f"{B['name']}, from {B['country']}, is a {B['description']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if answer == 'A':
        if A['follower_count'] > B['follower_count']:
            Score += 1
            print("Correct! Your score is now", Score)
            A = B
            B = random_option_B()
        else:
            print("Wrong! Final score:", Score)
            break
    elif answer == 'B':
        if B['follower_count'] > A['follower_count']:
            Score += 1
            print("Correct! Your score is now", Score)
            A = B
            B = random_option_B()
        else:
            print("Wrong! Final score:", Score)
            break
    else:
        print("Invalid input. Please type 'A' or 'B'.")
