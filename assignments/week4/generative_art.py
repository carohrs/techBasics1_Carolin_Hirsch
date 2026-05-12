from turtle import *
import random

# canvas size
width = 400
height = 400
setup(width, height)

#background color & border color
bgcolor("white")
color("black")

#flower pattern 10 times
for a in range(10):
    pendown()
    fillcolor(random.choice(["mediumaquamarine","lightcoral","lavender","lightskyblue","violet","palevioletred"]))
#condition
    if xcor() > 0 and ycor() > 0:
        fillcolor("black")
    #flower leaves
    for i in range(5):
        begin_fill()
        right(90)
        forward(70)
        right(40)
        forward(40)
        right(130)
        forward(40)
        right(30)
        forward(70)
        end_fill()
    #rerange for the circle to be in the middle of the flower
    penup()
    right(90)
    forward(25)
    right(90)
    forward(8)
    right(180)


    #circle (middle of the flower)
    pendown()
    fillcolor("yellow")
    begin_fill()
    circle(20)
    end_fill()
    penup()

    #new random position
    goto(random.randint(-200,200),random.randint(-200,200))


done()