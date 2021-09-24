from turtle import Screen
from player import Player
from car import Cars
import time


screen = Screen()
screen.setup(width=700, height=700)
screen.bgpic("background.gif")
screen.tracer(0)

player = Player()
cars = Cars()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.move()
    if cars.list_of_cars[-1].xcor() < -360:
        cars.create_cars()


screen.exitonclick()


