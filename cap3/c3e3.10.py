#Make a program that calculate the growth of a salary.It must request the value of the salary and the percentage of the growth.Show the value of the growth and of the new salary
salary=float(input("Insert your salary: "))
growth=float(input("Insert the Growth in porcentage: "))
nsalary=salary*((growth/100)+1)
print(f"Your new salary is ${nsalary:5.2f} with the growth of {growth}%")