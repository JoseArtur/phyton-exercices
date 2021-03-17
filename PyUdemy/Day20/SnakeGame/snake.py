from turtle import Turtle, Screen
class Snake():
    def __init__(self):

        self.parts = []
        self.create()
        self.head = self.parts[0]
    def create(self):
        for i in range(3):
            jonny = Turtle(shape="square")
            jonny.penup()
            jonny.color("white")
            jonny.setx(-20 * i)
            self.parts.append(jonny)
    def move(self):
        for seg_num in range(len(self.parts) - 1, 0, -1):
            # The new x and y will be the current x and y of the anterior square, e.g(if 3,
            # it will go to 2 pos)

            new_x = self.parts[seg_num - 1].xcor()
            new_y = self.parts[seg_num - 1].ycor()
            self.parts[seg_num].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        self.head.setheading(90) if self.head.heading()!=270 else 0
    def down(self):
        self.head.setheading(270) if self.head.heading()!=90 else 0
    def left(self):
        self.head.setheading(180) if self.head.heading()!=0 else 0
    def right(self):
        self.head.setheading(0) if self.head.heading() != 180 else 0