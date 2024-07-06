#from turtle import Turtle
from car import Car
import random

#COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_density = 10

    def create_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            #new_car.color(random.choice(COLORS))
            #random_y = random.randint(-250, 250)
            #new_car.goto(300, random_y)
            self.cars.append(Car())

    def move_cars(self):
        for car in self.cars:
            #car.backward(self.car_speed)
            car.move()
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)

    def increase_car_density(self):
        if self.car_density >= 4:
            self.car_density -= 1

    def level_up(self):
        self.car_speed += MOVE_INCREMENT




