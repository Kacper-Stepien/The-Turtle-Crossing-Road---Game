from turtle import Turtle
import random

Y_COORDINATE = [-165, -100, -35, 30, 100, 170]
COLORS = ["crimson", "indigo", "gold", "maroon", "navy", "alice blue", "royal blue", "dark slate blue", "deep pink",
          "indian red", "dark orange", "sea green", "cyan"]
START_X = [370, 380, 395, 415, 450]


class Cars:

    def __init__(self):
        self.distance = 3
        self.list_of_cars = []
        self.create_cars()

    def create_cars(self):
        self.list_of_cars = []
        for position in Y_COORDINATE:
            self.create_cars_on_one_traffic_lane(position)

    def create_cars_on_one_traffic_lane(self, y_position):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2.5)
        x = random.choice(START_X)
        y = y_position
        car.setheading(180)
        car.goto(x, y)
        self.list_of_cars.append(car)

        for i in range(0, 10):
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2.5)
            new_car.color(random.choice(COLORS))
            y = y_position
            x = self.list_of_cars[-1].xcor() + random.randint(50, 400)
            car.setheading(180)
            new_car.setposition(x, y)
            self.list_of_cars.append(new_car)

    def move(self):
        for car in self.list_of_cars:
            car.backward(self.distance)

    def increase_speed(self):
        self.distance += 2
