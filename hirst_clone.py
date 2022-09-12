# Hirst Painter Clone

import turtle as t
import random
from color_gen import art_colors  # import color list from generated colors from image

t.colormode(255)
benny = t.Turtle()
benny.speed("fastest")
benny.penup()
benny.hideturtle()

benny.setheading(225)
benny.forward(300)
benny.setheading(0)
number_dots = 100

for dot_count in range(1, number_dots + 1):
    benny.penup()
    benny.dot(20, random.choice(art_colors))
    benny.forward(50)

    if dot_count % 10 == 0:
        benny.setheading(90)
        benny.forward(50)
        benny.setheading(180)
        benny.forward(500)
        benny.setheading(0)

screen = t.Screen()
screen.exitonclick()
