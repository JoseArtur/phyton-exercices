# Write a program that ask the distance that a passsager desire run in km.Calculate the trip price, charging $0.5per km for trips until 200km and $0.45 for longer trips.
dist=int(input("What is the total distance of your trip: "))
if dist<=200:
    price=0.5*dist
else:
    price=0.45*dist
print(f"The price of your trip will be ${price}")