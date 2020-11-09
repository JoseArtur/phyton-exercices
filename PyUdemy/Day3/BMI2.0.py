height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight/(height**2)
if bmi<18.5:
  print(f"You are underweight and your BMI is {bmi:3.2f}")
elif bmi<25.0:
  print(f"You have a normal weight and your BMI is {bmi:3.2f}")
elif bmi<30.0:
  print(f"You are overweight and your BMI is {bmi:3.2f}")
elif bmi<35:
  print(f"You are obese and your BMI is {bmi:3.2f}")
else:
  print(f"You are clinically obese and your BMI is {bmi:3.2f}")