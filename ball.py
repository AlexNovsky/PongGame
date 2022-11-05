from turtle import Turtle
import time

SHAPE = "circle"
COLOR = "yellow"
UPPERWALL = 280
LOWERWALL = -280

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    # def UpRight(self):
    #     new_x = self.xcor() + self.x_move
    #     new_y = self.ycor() + self.y_move
    #     self.goto(new_x, new_y)

    # def Upleft(self):
    #     new_x = self.xcor() - 5
    #     new_y = self.ycor() + 5
    #     self.goto(new_x, new_y)
    #
    # def DownRight(self):
    #     new_x = self.xcor() + 5
    #     new_y = self.ycor() - 5
    #     self.goto(new_x, new_y)
    #
    # def DownLeft(self):
    #     new_x = self.xcor() - 5
    #     new_y = self.ycor() - 5
    #     self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()
