# Rewrite the last program to write the first 10 multiples of 3
typed=int(input("The first 10 multiples of 3 starting from: "))
x=typed
y=0
while x<=typed+11 or y<=9:
    if x%3==0:
        print(x)
        y=y+1
    x=x+1