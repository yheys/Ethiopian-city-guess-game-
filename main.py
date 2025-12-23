import turtle
from turtle import Turtle
import pandas


states=pandas.read_csv("50_states.csv")
state=states["city"].to_list()


screen=turtle.Screen()
screen.title("Ethiopian city Game")


image="animation.gif"
screen.addshape(image)
turtle.shape(image)

on_quize=True
answered_states=[]
while on_quize:
    answer=screen.textinput(title=f"Guess the City {len(answered_states)}/50",prompt="Enter the City name:").title()
    if answered_states==50:
        on_quize=False
        win = Turtle()
        win.penup()
        win.goto(int(states[states.city == answer]["x"].item()), int(states[states.city == answer]["y"].item()))
        win.hideturtle()
        win.write("You Are Winner")
    elif answer == "Exit":
        on_quize = False
        score = Turtle()
        score.penup()
        score.goto(-200, 0)
        score.hideturtle()
        score.write(f"You got {len(answered_states)} States from 50 States.", font=("Arial", 20,"bold"))
    elif answer in state and answer not in answered_states:
        name=Turtle()
        name.penup()
        name.goto(int(states[states.city==answer]["x"]),int(states[states.city == answer]["y"]))
        name.hideturtle()
        name.write(answer.title())
        answered_states.append(answer)














screen.exitonclick()


