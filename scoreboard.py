from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-215, 260)
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.level = 1
        self.write_score()

    def level_up(self):
        self.level += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", move=False, align=ALIGNMENT, font=FONT)
