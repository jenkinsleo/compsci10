#helper funcitons

def move_and_stamp(turtle):
    turtle.stamp()
    turtle.forward(16)

def origin(turtle):
    turtle.setheading(0)
    x,y = turtle.pos()
    x += 64
    return x,y

def move(turtle,n):
    for x in range(0,n):
        turtle.forward(16)


def draw_line(turtle, n):
    for x in range(0,n):
        move_and_stamp(turtle)


#digits
def draw_zero(turtle):
    x,y = origin(turtle)
    turtle.forward(16)

    for z in (2,4,2,4):
        draw_line(turtle,z)
        turtle.right(90)

    turtle.goto(x,y)

def draw_one(turtle):
    x,y = origin(turtle)

    move(turtle,3)
    turtle.right(90)
    draw_line(turtle,5)

    turtle.goto(x,y)

def draw_two(turtle):
    x,y = origin(turtle)

    turtle.forward(16)

    for z in ((2,turtle.right),(2,turtle.right),(2,turtle.left),(2,turtle.left),(3,turtle.left)):
        draw_line(turtle,z[0])
        z[1](90)

    turtle.goto(x,y)

def draw_three(turtle):
    x,y = origin(turtle)

    turtle.forward(16)
    draw_line(turtle,2)
    turtle.right(90)
    draw_line(turtle,4)
    turtle.right(90)
    draw_line(turtle,3)

    turtle.goto(x-48,y-32)
    turtle.setheading(0)
    draw_line(turtle,3)

    turtle.goto(x,y)

def draw_four(turtle):
    x,y = origin(turtle)

    turtle.forward(16)
    turtle.right(90)
    draw_line(turtle,2)
    turtle.left(90)
    draw_line(turtle,3)

    turtle.setheading(270)
    turtle.goto(x-16,y)
    draw_line(turtle,5)

    turtle.goto(x,y)
def draw_five(turtle):
    x,y = origin(turtle)

    move(turtle,3)
    turtle.left(180)
    for z in ((2,turtle.left),(2,turtle.left),(2,turtle.right),(2,turtle.right),(3,turtle.right)):
        draw_line(turtle,z[0])
        z[1](90)

    turtle.goto(x,y)

def draw_six(turtle):
    x,y = origin(turtle)

    move(turtle,3)
    turtle.left(180)
    for z in ((2,turtle.left),(2,turtle.left),(2,turtle.right),(2,turtle.right),(2,turtle.right),(2,turtle.right)):
        draw_line(turtle,z[0])
        z[1](90)
    turtle.goto(x,y)
def draw_seven(turtle):
    x,y = origin(turtle)

    turtle.forward(16)

    draw_line(turtle, 2)
    turtle.right(90)
    draw_line(turtle,5)

    turtle.goto(x,y)

def draw_eight(turtle):
    x,y = origin(turtle)

    turtle.forward(16)

    draw_line(turtle,2)
    turtle.right(90)
    draw_line(turtle,4)
    turtle.right(90)
    draw_line(turtle,2)
    turtle.right(90)
    draw_line(turtle,4)


    turtle.goto(x-48,y-32)
    turtle.setheading(0)
    draw_line(turtle,3)

    turtle.goto(x,y)
def draw_nine(turtle):
    x,y = origin(turtle)

    turtle.forward(16)

    draw_line(turtle,2)
    turtle.right(90)
    draw_line(turtle,4)
    turtle.right(90)
    draw_line(turtle,3)
    turtle.right(90)


    turtle.goto(x - (16*3), y - 16)
    turtle.stamp()


    turtle.goto(x-48,y-32)
    turtle.setheading(0)
    draw_line(turtle,3)

    turtle.goto(x,y)