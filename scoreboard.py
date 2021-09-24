from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.level = 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 28, "bold"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.display_level()

    def end_game(self):
        self.goto(0,0)
        self.color("crimson")
        self.write(f"GAME OVER", align="center", font=("Courier", 48, "bold"))