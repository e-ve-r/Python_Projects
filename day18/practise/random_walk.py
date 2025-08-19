from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.shape("turtle")
colormode(255)  # Enable RGB color mode
colors = ["red", "orange", "yellow", "green", "blue", "purple", "navy", "pink"]

directions = [0, 90, 180, 270] # facing right, up, left, down

timmy.pensize(15) #size of the pen
timmy.speed("fastest") # fastest drawing, accepts strings like "fastest", "fast", "normal", "slow", "slowest" and numbers 0-10

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for i in range(200):
    timmy.color(random_color()) # Set a random color
    timmy.forward(30)
    timmy.setheading(random.choice(directions)) # Randomly change direction