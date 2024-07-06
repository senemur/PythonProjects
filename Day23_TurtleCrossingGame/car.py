from turtle import Turtle
import random

SHAPE = ((-5, 0), (-3, 0), (-3, 5), (3, 5), (3, 0), (5, 0), (5, -4), (3, -4),
         (3, -5), (2, -5), (2, -4), (-2, -4), (-2, -5), (-3, -5), (-3, -4), (-5, -4))


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.colors = ["LavenderBlush1", "PeachPuff1", "Light Slate Blue", "lemon chiffon", "Light Green", "yellow", "Indian Red", "Plum", "Light Sky Blue"]
        self.penup()
        self.set_car_shape()
        self.color("black")
        self.fillcolor(random.choice(self.colors))
        self.goto(x=300, y=random.randint(-220, 220))

    def set_car_shape(self):
        self.getscreen().register_shape(name="car", shape=SHAPE)
        self.shape("car")
        self.left(90)
        self.shapesize(stretch_wid=4, stretch_len=2)

    def move(self):
        self.setx(self.xcor() - 10)
