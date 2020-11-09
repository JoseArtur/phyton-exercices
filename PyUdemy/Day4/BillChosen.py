import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lenNames = (len(names)-1)
rnumber=random.randint(0,int(lenNames))
print(f"{names[rnumber]} is going to pay the bill today!!")