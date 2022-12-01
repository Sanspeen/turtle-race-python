from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your beg", "Which turtle will win the race?")

colors = ["cyan", "blueviolet", "red", "green", "yellow", "darkgray"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []


def set_win_line():
    line_turtle = Turtle()
    line_turtle.color("green")
    line_turtle.width(20)
    line_turtle.penup()
    line_turtle.goto(230, 250)
    line_turtle.pendown()
    line_turtle.goto(230, -250)


for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    set_win_line()

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.color()
            if winner_color[0] == user_bet:
                print(f"You have won! The {winner_color[0]} turtle is the winner")
                break
            else:
                print(f"You've lost, The {winner_color[0]} turtle is the winner!")
                break

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
