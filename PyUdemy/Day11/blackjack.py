from art import logo
import random
decision = input("Do you want to play blackjack? 'y' or 'n':  ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def create_cards(name):
    random_card = cards[random.randint(0,12)]
    i=0
    while i<2:
        if not random_card in name:
            name.append(random_card)
            i+=1
        else:
            random_card = cards[random.randint(0,12)]
def add_card(name):
    i=0
    random_card = cards[random.randint(0,12)]
    while i<2:
        if not random_card in name:
            name.append(random_card)
            i+=1
        else:
            random_card = cards[random.randint(0,12)]  
    return name     
            
def verification(player,computer):
    if player== 21 and computer == 21:
        print("It's a draw")
    elif computer == 21:
        print(f"Computer wins")      
    elif player == 21 or computer>21:
        print("You are the winner!!!")
    elif player>21 or computer==21:
        print("Computer wins")
while decision == "y":
    print(logo)
    player =[]
    create_cards(player)
    player_score = sum(player)
    computer = []
    create_cards(computer)
    computer_score = sum(computer)
    verification(player_score, computer_score)        
    print(f"your cards: {player}, current score : {sum(player)}")
    print(f"computer's first card : {computer[0]} ")
    next_mov = input("TIME TO CHOOSE type 'y' to get acess to another card or 'n' to pass: ")
    if next_mov == "y ":
        add_card(player)
        verification(player_score,computer_score)
    something = input("Don't type: ")