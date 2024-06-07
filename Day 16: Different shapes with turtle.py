import random
from turtle import Screen, Turtle

colors = ["indianred", "deepskyblue", "cornflowerblue", "darkorchid", "seagreen", "wheat", "slategray", "lightseagreen"]

bruno = Turtle()
bruno.shape("turtle")

bruno.color(random.choice(colors))
for _ in range(3):
    bruno.forward(100)
    bruno.right(360/3)

bruno.color(random.choice(colors))
for _ in range(4):
    bruno.forward(100)
    bruno.right(360/4)

bruno.color(random.choice(colors))
for _ in range(5):
    bruno.forward(100)
    bruno.right(360/5)

bruno.color(random.choice(colors))
for _ in range(6):
    bruno.forward(100)
    bruno.right(360/6)

bruno.color(random.choice(colors))
for _ in range(7):
    bruno.forward(100)
    bruno.right(360/7)

bruno.color(random.choice(colors))
for _ in range(8):
    bruno.forward(100)
    bruno.right(360/8)

bruno.color(random.choice(colors))
for _ in range(9):
    bruno.forward(100)
    bruno.right(360/9)

bruno.color(random.choice(colors))
for _ in range(10):
    bruno.forward(100)
    bruno.right(360/10)


screen = Screen()
screen.exitonclick()import random
from turtle import Screen, Turtle