from turtle import Turtle
from random import randint
STARTING_X = 330


class Car(Turtle):

    def __init__(self, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=STARTING_X, y=randint(-250, 250))
