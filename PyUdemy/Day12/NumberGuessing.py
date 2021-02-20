import random
from logo import logo
print(logo)
def game():
    
    print("Welcome to the Number Guessing, here you have to \n find out a number between 1 and 100")
    difficult = input("Choose a difficult, 'easy' or 'hard': ")   
    def andnow():
        andnow = input("Would you like to restart? 'yes' or 'no' :")
        if andnow == "yes":
            game() 
        
            
    if difficult.lower() == "easy":
        attempts = 10
    elif difficult.lower() == "hard":
        attempts = 5
    else:
        print("This isn't a answer, try again")
        return 1
    random_number = random.randint(1,100)
    while attempts != 0:
        print(f"You have {attempts} remaining")
        guess = int(input("Guess a number: "))
        if guess == random_number:
            print("You win")
            andnow()
            return 1
        elif guess < random_number:
            print("Too low!!")
        elif guess > random_number:
            print("Too high!!")
        attempts-=1
    andnow()
game()