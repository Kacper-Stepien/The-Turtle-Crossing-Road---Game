from turtle import Turtle

DISTANCE = 20
COLOR = "green"
STARTING_POSTION = (0, -255)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(COLOR)
        self.penup()
        self.shapesize(1.5)
        self.setheading(90)
        self.goto(STARTING_POSTION)

    def move(self):
        self.forward(DISTANCE)