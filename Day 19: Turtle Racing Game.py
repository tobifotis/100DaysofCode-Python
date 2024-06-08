from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Welcome to the Annual Tobi Race. Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
random_number = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner 🎉")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner 🎉")

        rand_distance = random.choice(random_number)
        turtle.forward(rand_distance)

screen.exitonclick()
