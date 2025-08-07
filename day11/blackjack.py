import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)

while True:
    
    choice = input("Do you want to play the game of blackjack? type 'y' for yes and 'n' for no\n")
    while choice == 'y':
        
        user_cards = []
        computer_cards = []
        
        print("Welcome to the game of blackjack!")
        user_cards.append(deal_card())
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        computer_cards.append(deal_card())
        
        print(f"Your set of cards are: {user_cards}, your score is: {sum(user_cards)}")
        print(f"Computer's first card is: {computer_cards[0]}")
        
        another_round = input("Type 'y' to get another card, type 'n' to pass your turn \n")
        
        if another_round == 'y':
            user_cards.append(deal_card())
            if sum(computer_cards) < 17:
                computer_cards.append(deal_card())
                
        elif another_round == 'n':
            if sum(computer_cards) < 17:
                computer_cards.append(deal_card())
                
        print(f"Your set of cards are: {user_cards}, your score is: {sum(user_cards)}")
        print(f"Computer's set of cards are: {computer_cards}, computer's score is: {sum(computer_cards)}")
        if sum(user_cards) > 21:
            print("You went over 21, you lose!")
            break
        elif sum(computer_cards) > 21:
            print("Computer went over 21, you win!")
            break
        elif sum(user_cards) == 21:
            print("You got a blackjack, you win!")
            break
        elif sum(computer_cards) == 21:
            print("Computer got a blackjack, you lose!")
            break
        elif sum(user_cards) > sum(computer_cards):
            print("You win!")
            break
        elif sum(user_cards) < sum(computer_cards):
            print("You lose!")
            break
        else:
            print("It's a draw!")
            break
       
                
            
    

