from car import Car
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.movespeed = STARTING_MOVE_DISTANCE
        self.cars = []

    def spawn_car(self):
        car_color = choice(COLORS)
        car_move_speed = self.movespeed
        new_car = Car(color=car_color)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.movespeed
            car.goto(new_x, car.ycor())
            if car.xcor() < -330:
                self.cars.remove(car)
                car.clear()
                car.hideturtle()
                del car

    def add_level(self):
        self.movespeed += MOVE_INCREMENT
