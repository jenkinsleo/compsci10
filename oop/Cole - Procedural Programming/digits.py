from turtle import left, right, st
import turtle

def stamp_line(turtle, distance):
    for _ in range(distance):
        turtle.forward(16)
        turtle.stamp()

def stamp_right(turtle, distance):
    for _ in range(distance):
        stamp_line(turtle, 2)
        turtle.right(90)

def start(turtle):
    turtle.penup()
    turtle.forward(16)
    turtle.stamp()

def draw_zero(turtle):
    start(turtle)
    for _ in range(1, 3):
        stamp_right(turtle, 1)
        stamp_line(turtle, 4)
        turtle.right(90)
    turtle.forward(48)

def draw_one(turtle):
    turtle.penup()
    turtle.forward(48)
    turtle.right(90)
    turtle.stamp()
    stamp_line(turtle, 4)
    turtle.right(180)
    turtle.forward(64)
    turtle.right(90)
    turtle.forward(16)

def draw_two(turtle):
    start(turtle)
    stamp_right(turtle, 2)
    for _ in range(1,4):
        stamp_line(turtle, 2)
        turtle.left(90)
    turtle.forward(64)
    turtle.right(90)
    turtle.forward(16)

def draw_three(turtle):
    start(turtle)
    stamp_right(turtle, 3)
    turtle.right(90)
    stamp_right(turtle, 3)
    turtle.right(90)
    turtle.forward(48)
    turtle.left(90)
    turtle.forward(64)
    turtle.right(90)

def draw_four(turtle):
    start(turtle)
    turtle.right(90)
    for _ in range(1,4):
        stamp_line(turtle, 2)
        turtle.left(90)
    turtle.left(90)
    stamp_line(turtle, 4)
    turtle.backward(64)
    turtle.left(90)
    turtle.forward(16)

def draw_five(turtle):
    turtle.forward(48)
    turtle.right(180)
    turtle.stamp()
    for _ in range(1,4):
        stamp_line(turtle, 2)
        turtle.left(90)
    turtle.right(90)  
    for _ in range(1,3):
        turtle.right(90)
        stamp_line(turtle, 2)    
    turtle.backward(48)
    turtle.right(90)
    turtle.forward(64)
    turtle.right(90)


def draw_six(turtle):
    turtle.forward(48)
    turtle.right(180)
    turtle.stamp()
    for _ in range(1,3):
        stamp_line(turtle, 2)
        turtle.left(90)
    stamp_right(turtle, 4)
    turtle.forward(48)
    turtle.left(90)
    turtle.forward(32)
    turtle.right(90)

def draw_seven(turtle):
    start(turtle)
    stamp_line(turtle, 2)
    turtle.right(90)
    stamp_line(turtle, 4)
    turtle.backward(64)
    turtle.left(90)
    turtle.forward(16)

def draw_eight(turtle):
    start(turtle)
    stamp_right(turtle, 3)
    turtle.left(180)
    for _ in range(1,5):
        stamp_line(turtle, 2)
        turtle.left(90)
    turtle.right(180)
    stamp_line(turtle, 2)
    turtle.right(90)
    turtle.forward(48)

def draw_nine(turtle):
    start(turtle)
    stamp_right(turtle, 6)
    turtle.left(90)
    stamp_right(turtle, 2)
    turtle.forward(64)
    turtle.right(90)
    turtle.forward(48)

def draw_line(turtle, reps):
    for _ in range(reps):
        turtle.stamp()
        turtle.forward(16)