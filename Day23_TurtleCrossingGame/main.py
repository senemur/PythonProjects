import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkGray")
screen.tracer(0)

#dashed line
dashedline = Turtle()
dashedline.color("white")
dashedline.pensize(4)
def dashed_line():
    for i in range(50):
        dashedline.forward(30)
        dashedline.penup()
        dashedline.forward(30)
        dashedline.pendown()
dashedline.penup()
dashedline.goto(-300, 0)
dashedline.pendown()
dashed_line()


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()
        car_manager.car_speed *= 0.95
        if scoreboard.level % 3 == 0:
            car_manager.increase_car_density()




screen.exitonclick()