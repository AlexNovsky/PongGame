from turtle import Turtle
SHAPE = "square"
COLOR = "White"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
#        self.create_paddle()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
