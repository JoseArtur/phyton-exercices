# from turtle import Turtle, Screen
# jony = Turtle()
# jony.shape("turtle")
# jony.color("blue")
# jony.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charizard", "Fire"])
table.border = True
table.align = "r"
print(table)