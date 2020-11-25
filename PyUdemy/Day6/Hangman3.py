#Step 3

import random
from module import stages
from module import logo
from words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
from replit import clear
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
print(logo)
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.
live=6
verifier=[]
while "_" in display and live>0:
    
    guess = input("Guess a letter: ").lower()
    if guess in verifier:
        print(f"You have alredy but this letter ({guess}")
        pass
    verifier.append(guess)

#Check guessed letter
    count1=display.count("_")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    count2=display.count("_")
    if not guess in chosen_word:
        print(f"The letter {guess} is not in the word")
        print(stages[live-1])
        live-=1
    print(f"{' '.join(display)}")
if live>0:
    print("YOU WIN")
else:
    print("YOU LOST")
