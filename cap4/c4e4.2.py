# Write a program that ask the user car speed.If exceed 80km/h, show one message saying that the user has been fined.In this case, show the fine price, charging $5 per km over the limit of 80km/h
speed=int(input("What is your car speed(in km/h): "))
if speed>80:
    fine=(speed-80)*5
    print(f"You has been fined in ${fine}")
else:
    print("You're ok!!!")