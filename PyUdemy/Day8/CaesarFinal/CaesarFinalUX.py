alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(directionn,cypher_text, shift_amount):
  plain_text = ""
  for char in cypher_text:
     if char  in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                    new_position = position + shift_amount
            elif direction == "decode":
                    new_position = 26+position - shift_amount
            plain_text += alphabet[new_position]
     else:
            plaint_text+=char
  print(f"Here's the {direction}d result: {plain_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'. 


#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Hint: Think about how you can use the modulus (%).
x=True
while x is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%25
    caesar(cypher_text=text, shift_amount=shift, directionn=direction)
    restart=input("Do you want to go again? yes or no ")
    if restart=="yes":
        x=True
    else:
        x=False
        print("Goodbye")

    
