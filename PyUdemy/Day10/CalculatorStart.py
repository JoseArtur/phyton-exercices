#logo
from art import logo
def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations = {
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))
    for key in operations:
        print(key)
    decision="y"
    while decision == "y": 
        operation_key = input("Pick operation symbol: ")
        next_num = float(input("What's the next number: "))
        calculation_function = operations[operation_key]
        answer = calculation_function(num1,next_num)
        prev_answer=answer
        print(f"{num1}{operation_key}{next_num}={prev_answer}")
        if "y" == input("Type 'y' to continue calculating with {answer}, or type 'n' to exit: "):
            num1 = answer
        else:
            calculator()
    print("Thanks you for using")
calculator()