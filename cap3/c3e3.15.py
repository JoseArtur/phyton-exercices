#Write a program that calculate the reduction of a smoker's livetime.
# Ask the quantity of cigarettes smoked per day and how many years he/she had smoked.Consider that the smoker lost 10 minutes of live each cigarrette, and calculate how many days of live the smoker will lost.Show the total of days
cig=int(input("How many cigarrettes smoked per day: "))
years=int(input("How many years has smoked: "))
days=((10*cig)*365*years)/(60*24)
print(f"{days:5.2f} days has been losted.STOP SMOKING")