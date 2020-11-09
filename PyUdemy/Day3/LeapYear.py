year = int(input("Put a year to check if it's a Leap Year!:"))

if year%4==0:
  if year%100==0:
    if year%400==0:
      print(f"{year} is a Leap Year!!")
    else:
      print(f"{year} is a NOT Leap Year!!")
  else:
    print(f"{year} is a  Leap Year!!")
else:
    print(f"{year} is a Leap Year!!")