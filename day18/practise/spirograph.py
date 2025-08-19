import pickle
from turtle import Turtle, Screen, colormode, setheading
import random
colormode(255)

oggy = Turtle()

oggy.speed("fastest")
oggy.shape("turtle")

def pick_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        current_heading = oggy.heading()
        oggy.setheading(current_heading+size_of_gap)
        oggy.color(pick_color())
        oggy.circle(100)
    
draw_spirograph(5)
 
screen = Screen()    
screen.exitonclick()