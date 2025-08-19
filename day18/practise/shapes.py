from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "navy", "pink"]

for i in range(3, 11):

    angle = 360/i
    
    timmy.color(random.choice(colors))
    
    for j in range(0,i):
        timmy.forward(100)
        timmy.right(angle)



screen = Screen()
screen.exitonclick()
