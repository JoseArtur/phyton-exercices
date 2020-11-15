for number in range(0,101):
  if number%3==0 and number%5==0: #This has to be in the first if-elif sequence
    print("FizzBuzz")
  elif number%3==0:
    print("Fizz")
  elif number%5==0:
    print("Buzz")
  else:
    print(number)