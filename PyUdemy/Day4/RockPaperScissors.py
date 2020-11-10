import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
pychoice=int(input("Choose!!! Type 0 for rock, 1 for paper and 2 for scissors: "))
cpchoice=random.randint(0,2)
list=[rock,paper,scissors]
if pychoice<0 or pychoice>=3:
  print("You typed an invalid number.")
if  pychoice==0 and cpchoice==2:
  print(list[cpchoice])
  print(list[pychoice])
  print("You win")
elif   pychoice==2 and cpchoice==0:
  print(list[cpchoice])
  print(list[pychoice])
  print("You Lose")
elif cpchoice>pychoice:
  print(list[cpchoice])
  print(list[pychoice])
  print("You lose")
elif pychoice==cpchoice:
  print(list[cpchoice])
  print(list[pychoice])
  print("It's a draw")
elif pychoice>cpchoice:
  print(list[cpchoice])
  print(list[pychoice])
  print("You win")
else:
  print("You typed an invalid number.")


