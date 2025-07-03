import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome! to Rock, Paper & Scissors Game\n")
choice = int(input("Choose 1 for Rock, 2 for Paper & 3 for Scissors\n"))

comp = random.randint(1,3)

if comp == 1:
    print("The Computer Chose\n"+rock+"\n")
elif comp == 2:
    print("The Computer Chose\n"+paper+"\n")
elif comp == 3:
    print("The Computer Chose\n"+scissors+"\n")

if choice == 1:
    print("You Choose:\n"+rock+"\n")
    
elif choice == 2:
    print("You Choose:\n"+paper+"\n")
    
elif choice == 3:
    print("You Choose:\n"+scissors+"\n")
    
else:
    print("Invalid Choice!")


if(choice == 1 and comp == 2 or choice == 2 and comp == 3 or choice == 3 and comp == 1):
    print("Computer Won!\n")

elif(choice == 1 and comp == 3 or choice == 2 and comp == 1 or choice == 3 and comp == 2):
    print("You Won!\n")
    
elif choice == comp:
    print("It's a Tie!\n")
    
else:
    print("Invalid Choice!\n")