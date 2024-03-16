import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

## This is for drawing square:
# for i in range(4):
#     tim.forward(200)
#     tim.right(90)  #kaç derece döneceği yazılır


## This is for drawing dashed line:
# for i in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


## This is for drawing a triangle, square, pentagon, hexagon...
# colors = ["gainsboro","medium sea green","deep sky blue","red","yellow","orange","magenta","salmon","dark khaki","cornflower blue","lime","maroon","olive drab"]
# def draw_shape(num_sides):
#     angle= 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


## This is for drawing a random walk:
# colors = ["alice blue","medium sea green","deep sky blue","spring green","light pink","plum","hot pink","dark sea green","khaki","cornflower blue","light sea green","light sky blue","pale green"]
# directions= [0, 90, 180,270]
# tim.pensize(10)
# for i in range(300):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# # This is for drawing a spirograph with random rgb colors
# turtle.colormode(255)
# tim.speed("fastest")
# def random_colors():
#     r= random.randint(0, 255)
#     g= random.randint(0, 255)
#     b= random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
# def draw_spirograph(size_of_gap):
#     for i in range(int(360/ size_of_gap)):
#         tim.color(random_colors())
#         tim.circle(100)
#         tim.right(10) # this step could also be done like this: tim.setheading(tim.heading()+size_of_gap)
# draw_spirograph(5)





screen = Screen()
screen.exitonclick()
