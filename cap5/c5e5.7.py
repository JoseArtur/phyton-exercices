# Modiy the last program of a way that he user also type the start and the end of the multiplication table, instead of start from 1 and 10.
x=int(input("Type a number to the multiplication table: "))
start=int(input("Type start number: "))
end=int(input("Type the end number: "))
n=1
y=start
while n<=(end+1-start):
    print(f"{x}X{y}={x*y}")
    n=n+1
    y=y+1