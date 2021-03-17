from turtle import Turtle, Screen

jonny = Turtle()
screen = Screen()

def move_forward():
    jonny.forward(10)
def move_backward():
    jonny.forward(-10)
def counter_clockwise():
    x = jonny.heading()
    jonny.setheading(x+5)
def clockwise():
    x = jonny.heading()
    jonny.setheading(x-5)

def clear():
    jonny.clear()
    jonny.penup()
    jonny.home()
    jonny.pendown()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a",fun=counter_clockwise)
screen.onkeypress(key="d",fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()