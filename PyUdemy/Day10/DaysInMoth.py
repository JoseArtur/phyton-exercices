def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return("Leap year.")
      else:
        return("Not leap year.")
    else:
      return("Leap year.")
  else:
    return("Not leap year.")

def days_in_month(year,month):
    
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  verifier = is_leap(year)
  if verifier == "Leap Year":
      month_days[1]=29
      days=month_days[month-1]
  else:
      days=month_days[month-1]
  return days
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


