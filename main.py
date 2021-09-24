from turtle import Screen
from player import Player


screen = Screen()
screen.setup(width=700, height=700)
screen.bgpic("background.gif")

player = Player()


screen.listen()
screen.onkey(player.move, "Up")

screen.exitonclick()


