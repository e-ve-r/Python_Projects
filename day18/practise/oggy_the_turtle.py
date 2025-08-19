from turtle import Turtle, Screen

oggy = Turtle()
oggy.shape("turtle")
oggy.color("blue")

#printing a square using turtle graphics
oggy.forward(100)
oggy.right(90)
oggy.forward(100)
oggy.right(90)
oggy.forward(100)
oggy.right(90)
oggy.forward(100)

#drawing dashed lines
# for i in range(50):
#     oggy.pendown()
#     oggy.forward(10)
#     oggy.penup()
#     oggy.forward(10)

screen = Screen()
screen.exitonclick()


