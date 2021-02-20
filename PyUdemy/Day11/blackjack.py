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
    while i<1:
        if not random_card in name:
            name.append(random_card)
            i+=1
        else:
            random_card = cards[random.randint(0,12)]  
    return name     
            
def verification(playerr,computerr):
    if playerr== 21 and computerr == 21:
        print("It's a draw")
    elif computerr == 21:
        print(f"your final  cards: {player}, final score : {playerr}")
        print(f"Computer's final hand: {computer}, final score: {computerr}")
        print(f"Computer wins")      

        decision =input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        restart(player,computer)
    elif playerr == 21 or computerr>21:
        print(f"your final  cards: {player}, final score : {playerr}")
        print(f"Computer's final hand: {computer}, final score: {computerr}")
        print("Opponent went over. You win 😁") 
        decision =input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        restart(player,computer)

        
    elif playerr>21 or computerr==21:
        print(f"your final  cards: {player}, final score : {playerr}")
        print(f"Computer's final hand: {computer}, final score: {computerr}")
        print("Computer wins")

        decision =input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")        
        restart(player,computer)

def restart(player,computer):
    player=[]
    computer = []
    return player
    return computer
if decision != "y":
    pass         
print(logo)

while decision == "y":
    player =[]
    create_cards(player)
    player_score = sum(player)
    computer = []
    create_cards(computer)
    player_score = sum(player)

    computer_score = sum(computer)
    verification(player_score, computer_score)        
    print(f"your cards: {player}, current score : {sum(player)}")
    print(f"computer's first card : {computer[0]} ")
    next_mov = input("TIME TO CHOOSE type 'y' to get acess to another card or 'n' to pass: ")
    while next_mov == "y":
        add_card(player)
        add_card(computer)
        player_score = sum(player)
        computer_score = sum(computer)
        verification(player_score,computer_score)
        print(f"your cards: {player}, current score : {sum(player)}")
        print(f"computer's first card : {computer[0]} ")
        next_mov = input("TIME TO CHOOSE type 'y' to get acess to another card or 'n' to pass: ")
    
    while next_mov != "y":
        add_card(computer)
        computer_score = sum(computer)
        verification(player_score,computer_score)

    something = input("Don't type: ")