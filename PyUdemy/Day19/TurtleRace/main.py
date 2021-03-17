from turtle import Turtle, Screen
import random
import symtable
screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make your bet ", prompt="Whick turtle will win the race? Select a color:")
turtles = []
colors = ["red","blue", "yellow", "purple", "orange"]
positions = [-70,-40,-10,20,50]
for index in range(5):
    jonny = Turtle(shape="turtle")
    jonny.color(colors[index])
    jonny.penup()
    jonny.goto(x=-240,y=positions[index])
    turtles.append(jonny)
race_on = False
if bet in colors:
    race_on = True
while race_on:
    for turtle in turtles:
        random_number = random.randint(0, 30)
        turtle.forward(random_number)
        if turtle.xcor() >= 225:
            if turtle.color()[0] == bet:

                print(f"Your {turtle.color()[0]} turtle win, Congratulations!!")
            else:
                print(f"You lose.The {turtle.color()[0]} turtle win ")
            race_on = False

screen.exitonclick()
