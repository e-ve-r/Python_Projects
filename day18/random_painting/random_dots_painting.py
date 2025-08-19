import random
from turtle import Turtle, Screen, colormode

colormode(255)
# colors = colorgram.extract('day18/random_painting/image.png', 20)
# colors_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     colors_list.append(new_color)
#     print(colors_list)

colors_list = [
    (234, 225, 83),
    (195, 8, 69),
    (231, 54, 132),
    (194, 164, 15),
    (112, 178, 214),
    (199, 77, 15),
    (216, 162, 101),
    (34, 187, 112),
    (29, 104, 167),
    (14, 23, 64),
    (20, 29, 168),
    (212, 136, 175),
    (231, 224, 7),
    (197, 34, 130),
    (15, 181, 210),
    (231, 167, 197),
]

oggy = Turtle()
oggy.speed("fastest")

screen = Screen()

oggy.penup()

width = screen.getcanvas().winfo_width() / 2
height = screen.getcanvas().winfo_height() / 2
oggy.goto(-width + 20, height - 20)

for i in range(10):
    for j in range(10):
        oggy.dot(20, random.choice(colors_list))
        oggy.forward(50)
    oggy.right(90)
    oggy.right(90)
    oggy.forward(500)
    oggy.left(90)
    oggy.forward(50)
    oggy.left(90)

oggy.hideturtle()

screen.exitonclick()
