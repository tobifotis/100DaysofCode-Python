import turtle
from turtle import Turtle, Screen
import random

colors = ["indianred", "deepskyblue", "cornflowerblue", "darkorchid", "seagreen", "wheat", "slategray", "lightseagreen"]
direction = [0, 90, 180, 270]

kobe = Turtle()
turtle.colormode(255)
kobe.shape("turtle")
kobe.color("cornflowerblue")
kobe.pensize(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    topper = (r, g, b)
    return topper


for _ in range(200):
    kobe.color(random_color())
    kobe.forward(30)
    kobe.speed(0)
    kobe.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
