import turtle
import colorgram
from turtle import Turtle,Screen, shape
import random

rgb_color = []
turtle.colormode(255)
colors = colorgram.extract('image.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_color.append(new_color)

tim = Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed('fastest')
tim.hideturtle()

number_of_dot = 100
for dot_count in range(1, number_of_dot+1):
    tim.dot(20,random.choice(rgb_color))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen  = Screen()
screen.exitonclick()