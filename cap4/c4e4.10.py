# Write a program that calculate the price to pay for the eletric energy supply.Ask the quantity of consumed KWh abd the installation type: R for residencies, I for Industries and M for Markets.Calculate the price to pay according the following table.
kwh=float(input("Insert the KWh Consumation: "))
inst=input("\n1-Residencial\n2-Markets\n3-Industrial\nInsert the type of installation in your home: ")
if inst=="1":
    if kwh<=500:
        price=0.4*kwh
    else:
        price=0.65*kwh
elif inst=="2":
    if kwh<=500:
        price=0.55*kwh
    else:
        price=0.6*kwh
elif inst=="3":
    if kwh<=500:
        price=0.55*kwh
    else:
        price=0.6*kwh
print(f"The price to pay will be ${price}")