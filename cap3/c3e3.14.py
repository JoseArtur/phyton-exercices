#Write a program that ase the quantity in km traveled by a rented car,as the quantity of days that the car was rented.Calculate the price to pay, knowing that the car cost $6 for day and $0.15 p/km traveled.
km=int(input("Type the quantity of km traveled with the rented car(in km): "))
days=int(input("Type the quantity of days  that the car wa rented: "))
price=(6*days)+(0.15*km)
print(f"The price to pay is ${price}")