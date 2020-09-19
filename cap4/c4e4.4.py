# Write a program that ask the worker salary and calculate the salary's growth.For salaries over $1250,00, calculate a growth of 10%.For under or equal, of 15%
salary=float(input("What's your salary: "))
base=salary
if salary>1250:
    nsalary=(base*1.1)
else:
    nsalary=base*1.15
print(f"Your salary of ${salary}, now will be ${nsalary}")