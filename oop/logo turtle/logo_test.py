##2020-01-27

import logo
import turtle

screen = turtle.Screen()
myrtle = turtle.Turtle()
myrtle.speed(0)
screen = turtle.Screen()
screen.bgcolor('white')

def draw_box(x,y, scale = 1, angle = 0):
    myrtle.setheading(0)
    myrtle.penup()
    myrtle.goto(x, y)
    myrtle.left(angle)
    myrtle.pendown()
    for i in range(0,4):
        myrtle.forward(logo.STANDARD_LOGO_SIZE * scale)
        myrtle.right(90)

# **** test 1: draw a logo with scale 1 and angle 0
x = logo.STANDARD_LOGO_SIZE * -1
y = logo.STANDARD_LOGO_SIZE 
scale = 1

draw_box(x, y, scale, 0)
logo.draw_logo(x, y, scale, 0)

# **** test 2: draw a logo with scale 1 and rotated one quarter turn left  ****
x = logo.STANDARD_LOGO_SIZE
y = logo.STANDARD_LOGO_SIZE
angle = -90

draw_box(x, y, scale, angle)
logo.draw_logo(x, y, scale, angle)

# **** test 3: draw a logo with scale 0.5 and angle 0 ****
# note that angle is not specified for logo.draw
x = logo.STANDARD_LOGO_SIZE * -0.5
y = 0
scale = 0.5
angle = 0

draw_box(x, y, scale, angle)
logo.draw_logo(x, y, scale)

# **** test 4: draw a logo with scale 0.5 and angle -45 ****
# note that the angle is being passed in as a 'literal' instead of 
# as a variable. this is perfectly acceptable; the previous tests
# passed in a variable only for the sake of readability.
x = logo.STANDARD_LOGO_SIZE * 0.5
y = 0

draw_box(x, y, scale, -45)
logo.draw_logo(x, y,scale, -45)


# **** test 5: draw a logo with scale and angle not specified
# should be the equivalent to test 1
x = logo.STANDARD_LOGO_SIZE * -1
y = logo.STANDARD_LOGO_SIZE 
scale = 1

logo.draw_logo(x, y)


screen.exitonclick()
