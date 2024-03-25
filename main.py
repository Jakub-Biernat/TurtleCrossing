import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=1000, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()

    if player.ycor() > FINISH_LINE_Y:
        player.starting_position()
        scoreboard.level_up()
        car_manager.add_level()

