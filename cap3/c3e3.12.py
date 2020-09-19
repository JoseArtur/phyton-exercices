#Write a program that calculate the time of a car trip.Ask the distance to go and the medium speed waited for the trip.
dist=int(input("Type the distance of the trip(in km):"))
speed=int(input("Type the medium speed waited(in km/h): "))
time=dist/speed
print(f"The duration of the trip will be {time} hours")