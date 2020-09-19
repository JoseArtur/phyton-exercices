#Write a program that read the quantity of days, hours, minutes and seconds of the user.Calculate the total in seconds
days=int(input("Type the quantity of days: "))
second=days*24*60*60
hours=int(input("Type the quantity of hours: "))
second=second+(hours*60*60)
minutes=int(input("Type the quantity of minutes: "))
second=second+(minutes*60)
seconds=int(input("Type the quantity of seconds: "))
second=second+(seconds)
print(f"The total in seconds is {second}")
