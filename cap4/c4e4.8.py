# Write a progream that read two numbers and ask which operation you desire make.You must can calculate sum(+), subtration(-), multiplication(*) and division (/).Show the asked operation result.
n1=int(input("Type the first number: "))
n2=int(input("Type the second number: "))
op=input("Type your chosen operation (+,-,X,/): ")
if op=="+":
    re=n1+n2
elif op=="-":
    re=n1-n2
elif op=="X":
    re=n1*n2
elif op=="/":
    re=n1/n2
print(f"The result of {n1}{op}{n2} is {re}")