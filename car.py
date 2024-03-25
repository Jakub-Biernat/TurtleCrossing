from turtle import Turtle
from random import randint
STARTING_X = 330


class Car(Turtle):

    def __init__(self, color, move_speed):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.move_speed = move_speed
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=STARTING_X, y=randint(-260, 260))

    def move(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x, self.ycor())




