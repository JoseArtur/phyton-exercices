# Program 4.3 - Brazilian Income Tax Calculator
salary=float(input("Type your salary:R$ "))
base=salary
tax=0
if base>3000:
    tax=tax+((base-3000))*0.35
    base=3000
if base>1000:
    tax=tax+((base-1000)*0.2)
print(f"Salary::R${salary:6.2f} Tax to pay: R${tax:6.2f}")
