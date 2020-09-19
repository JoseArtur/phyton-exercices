# Change the last program to show the results at the same format of a multiplication table: 22x1=2, 2x2=4...
x=int(input("Insira o nome para a tabuada: "))
y=1
while y<=10:
    print(f"{x}X{y}={x*y}")
    y=y+1