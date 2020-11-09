year = int(input())

if year%4==0:
  cond=True
if year%100==0 and cond==True:
  cond=False
if year%400==0 and cond==False:
  print(f"{year} is a Leap Year!!")
else:
  print(f"{year} is not a Leap Year")