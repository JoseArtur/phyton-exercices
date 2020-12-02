def prime_checker(number):
    x=1
    count=0
    while x<=number:
        if number%x==0:
            count+=1
        x+=1
    if count==2:
        print("This is a prime number")
    else:
        print("This is not a prime number")