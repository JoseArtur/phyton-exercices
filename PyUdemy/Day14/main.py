#Import things
from art import logo,vs
import data
from random import randint
#Creating the main funcion called game
global score
score = 0
random = data.data[randint(0,49)]
Brandom = data.data[randint(0,49)]
current = True

def compare(answer,random,Brandom,sco,current):
    if answer.lower()=="a":
        if int(random['follower_count']) >int(Brandom['follower_count']):
            sco+=1
            current=True
        else:
            print("You Lost")
            current = False
            
    elif answer.lower() =="b":
        if int(Brandom['follower_count']) >int(random['follower_count']):
            sco+=1
            current=True
        else:
            print("You Lost")
            current = False
    return current,sco
def compare_random(random,Brandom):
    if random==Brandom:
        random = data.data[randint(0,49)]
    return random
def game(random,Brandom,score,current):
    
    if score!=0:
        print(f"You're right! Your current score is {score}")
    B = f"Against B: {Brandom['name']}, a {Brandom['description']} from {Brandom['country']}"
    A = f"compare A: {random['name']}, a {random['description']} from {random['country']}"
    print(A)
    print(vs)
    print(B)
    answer =input("Who has more followers?: ")
    
    current,score = compare(answer,random,Brandom,score,current)
    #Here I verifie if the current status is to move on or to stop the game
    print(current)
    if current==False:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        return 1
    #Now random become Brandom
    Brandom =random
    if random==Brandom:
        random = data.data[randint(0,49)]
        
    game(random,Brandom,score,current)
    
    
    
    
    
    
print(logo)
game(random,Brandom,score,current)