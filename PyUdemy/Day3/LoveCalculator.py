# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count_t =name1.lower().count("t")+name2.lower().count("t")
count_r =name1.lower().count("r")+name2.lower().count("r")
count_u =name1.lower().count("u")+name2.lower().count("u")
count_e =name1.lower().count("e")+name2.lower().count("e")
count_true=count_t+count_r+count_u+count_e
count_l =name1.lower().count("l")+name2.lower().count("l")
count_o =name1.lower().count("o")+name2.lower().count("o")
count_v =name1.lower().count("v")+name2.lower().count("v")
count_e1 =name1.lower().count("e")+name2.lower().count("e")
count_love=count_l+count_o+count_v+count_e
score=count_true*10+count_love
if  score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")