# Write a program that aproves the banking loan for buy a house.
# The program must ask the house to pay price, the salary and the quantity of years to pay. The mensal installment can't be superior to 30% of the salary. 
# Calculate the installment value as being the house to pay house divided por the number of months to pay
value=float(input("Insert the value of your pretended house: "))
salary=float(input("Insert your salary: "))
years=int(input("Insert how many years you pretend to pay: "))
prest=(value/years)/12
if prest<0.3*salary:
    print(f"With your salary of {salary} you will have to pay ${prest:5.2f} for {years*12}")
else:
    print("Your salary isn't enought, the prestation must be loweer than 30% of your salary")