from turtle import *
import random

#define constants
WIDTH = 400
HEIGHT = 400
BGCOLOR = "white"
PENCOLOR = "black"

#define global variable
paint_process = False

# setup canvas size
setup(WIDTH, HEIGHT)

#background color & border color
bgcolor(BGCOLOR)
color(PENCOLOR)

def randomize_fillcolor():
    return random.choice(["mediumaquamarine", "lightcoral", "lavender", "lightskyblue", "violet", "palevioletred","yellow"])

def draw_flower_leaves():
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
def draw_circle():
    # rerange for the circle to be in the middle of the flower
    penup()
    right(90)
    forward(25)
    right(90)
    forward(8)
    right(180)

    # circle (middle of the flower)
    pendown()
    fillcolor(randomize_fillcolor())
    begin_fill()
    circle(20)
    end_fill()
    penup()

# function to create pattern with n flowers
def draw_flower_pattern(n:int,color:str = "black"):
    for a in range(n):
        pendown()
        fillcolor(randomize_fillcolor())
        # condition
        if xcor() > 0 and ycor() > 0:
            fillcolor(color)
        draw_flower_leaves()
        draw_circle()
        # new random position
        goto(random.randint(-200, 200), random.randint(-200, 200))

    done()

if __name__ == '__main__':
    decision = input("Do you want to see the paint process? (Yes/No)").lower()
    if decision == "yes":
        paint_process = True
    if paint_process == False:
        tracer(0, 0)

    draw_flower_pattern(20, "pink")