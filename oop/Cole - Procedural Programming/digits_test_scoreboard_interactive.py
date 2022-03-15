import turtle
import digits

GRID_SIZE = 16

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(GRID_SIZE * 53, GRID_SIZE * 19)

home_turtle = turtle.Turtle()
home_turtle.hideturtle()
home_turtle.speed(0)
home_turtle.shapesize(0.5,0.5)
home_turtle.shape('circle')
home_turtle.pencolor('yellow')
home_turtle.fillcolor('yellow')
home_turtle.hideturtle()
home_turtle.penup()

away_turtle = home_turtle.clone()
minutes_turtle = home_turtle.clone()
seconds_turtle = home_turtle.clone()

ball_on_turtle = home_turtle.clone()
ball_on_turtle.pencolor('red')
ball_on_turtle.fillcolor('red')

down_turtle = ball_on_turtle.clone()
to_go_turtle = ball_on_turtle.clone()
quarter_turtle = ball_on_turtle.clone()

LEFT_EDGE = wn.window_width() * -0.5 + GRID_SIZE * 1
TOP_EDGE = wn.window_height() * 0.5 - GRID_SIZE

def draw_labels():

    myrtle = turtle.Turtle()
    myrtle.shape('square')
    myrtle.shapesize(0.5,0.5)
    myrtle.fillcolor('white')
    myrtle.pencolor('white')
    myrtle.penup()
    myrtle.speed(0)

    #OUTLINE
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 0.0), TOP_EDGE - (GRID_SIZE * 0.0))
    myrtle.pendown()
    for i in range(2):
        myrtle.forward(GRID_SIZE * 51)
        myrtle.right(90)
        myrtle.forward(GRID_SIZE * 17)
        myrtle.right(90)

    #HOME LABEL
    myrtle.penup()
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 3), TOP_EDGE - (GRID_SIZE * 2))
    myrtle.write("HOME", True, align="left", font=("Arial", 16, "normal"))

    #TIME LABEL
    myrtle.penup()
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 23), TOP_EDGE - (GRID_SIZE * 2))
    myrtle.write("TIME", True, align="left", font=("Arial", 16, "normal"))
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 25), TOP_EDGE - (GRID_SIZE * 4))
    myrtle.stamp()
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 25), TOP_EDGE - (GRID_SIZE * 6))
    myrtle.stamp()
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 17), TOP_EDGE - (GRID_SIZE * 2.5))
    myrtle.pendown()
    for i in range(2):
        myrtle.forward(GRID_SIZE * 16)
        myrtle.right(90)
        myrtle.forward(GRID_SIZE * 5)
        myrtle.right(90)

    #AWAY LABEL
    myrtle.penup()
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 43), TOP_EDGE - (GRID_SIZE * 2))
    myrtle.write("AWAY", True, align="left", font=("Arial", 16, "normal"))

    #BALL ON LABEL
    myrtle.penup()
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 5), TOP_EDGE - (GRID_SIZE * 10))
    myrtle.write("BALL ON", True, align="left", font=("Arial", 16, "normal"))

    #DOWN LABEL
    myrtle.penup()
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 20), TOP_EDGE - (GRID_SIZE * 10))
    myrtle.write("DOWN", True, align="left", font=("Arial", 16, "normal"))

    #TO GO LABEL
    myrtle.penup()
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 32), TOP_EDGE - (GRID_SIZE * 10))
    myrtle.write("TO GO", True, align="left", font=("Arial", 16, "normal"))

    #QUARTER LABEL
    myrtle.penup()
    myrtle.setpos(LEFT_EDGE + (GRID_SIZE * 41), TOP_EDGE - (GRID_SIZE * 10))
    myrtle.write("QUARTER", True, align="left", font=("Arial", 16, "normal"))


def parse_value(value):
    if value is None:
        return (0,0)
    else:
        try:
            value_as_int = int(value)
        except:
            value_as_int = 0
        tens = int(value_as_int / 10)
        ones = value_as_int % 10
        return (tens, ones)

def draw_digit(digit, turtle_to_use):
    if (digit == 1):
        digits.draw_one(turtle_to_use)
    elif (digit == 2):
        digits.draw_two(turtle_to_use)
    elif (digit == 3):
        digits.draw_three(turtle_to_use)
    elif (digit == 4):
        digits.draw_four(turtle_to_use)
    elif (digit == 5):
        digits.draw_five(turtle_to_use)
    elif (digit == 6):
        digits.draw_six(turtle_to_use)
    elif (digit == 7):
        digits.draw_seven(turtle_to_use)
    elif (digit == 8):
        digits.draw_eight(turtle_to_use)
    elif (digit == 9):
        digits.draw_nine(turtle_to_use)
    else:
        digits.draw_zero(turtle_to_use)
        
def draw_home():
    score = wn.numinput("HOME", "", default=0, minval=0, maxval=99)
    digits = parse_value(score)
    home_turtle.clearstamps()
    home_turtle.penup()
    home_turtle.setpos(LEFT_EDGE + (GRID_SIZE * 1), TOP_EDGE - (GRID_SIZE * 3))
    draw_digit(digits[0], home_turtle)
    draw_digit(digits[1], home_turtle) 
    wn.listen()
    
def draw_away():
    score = wn.numinput("AWAY", "", default=0, minval=0, maxval=99)
    digits = parse_value(score)
    away_turtle.clearstamps()
    away_turtle.penup()
    away_turtle.setpos(LEFT_EDGE + (GRID_SIZE * 41), TOP_EDGE - (GRID_SIZE * 3))
    draw_digit(digits[0], away_turtle)
    draw_digit(digits[1], away_turtle)
    wn.listen()

def draw_minutes():
    minutes = wn.numinput("MINUTES", "", default=0, minval=0, maxval=15)
    digits = parse_value(minutes)
    minutes_turtle.clearstamps()
    minutes_turtle.penup()
    minutes_turtle.setpos(LEFT_EDGE + (GRID_SIZE * 17), TOP_EDGE - (GRID_SIZE * 3))
    draw_digit(digits[0], minutes_turtle)
    draw_digit(digits[1], minutes_turtle)
    wn.listen()

def draw_seconds():
    score = wn.numinput("SECONDS", "", default=0, minval=0, maxval=59)
    digits = parse_value(score)
    seconds_turtle.clearstamps()
    seconds_turtle.penup()
    seconds_turtle.setpos(LEFT_EDGE + (GRID_SIZE * 25), TOP_EDGE - (GRID_SIZE * 3))
    draw_digit(digits[0], seconds_turtle)
    draw_digit(digits[1], seconds_turtle)
    wn.listen()    

def draw_ball_on():
    score = wn.numinput("BALL ON", "", default=0, minval=1, maxval=55)
    digits = parse_value(score)
    ball_on_turtle.clearstamps()
    ball_on_turtle.penup()
    ball_on_turtle.setpos(LEFT_EDGE + (GRID_SIZE * 4), TOP_EDGE - (GRID_SIZE * 11))
    draw_digit(digits[0], ball_on_turtle)
    draw_digit(digits[1], ball_on_turtle)
    wn.listen()    

def draw_down():
    score = wn.numinput("DOWN", "", default=1, minval=1, maxval=4)
    digits = parse_value(score)
    down_turtle.clearstamps()
    down_turtle.penup()
    down_turtle.setpos(LEFT_EDGE + (GRID_SIZE * 20), TOP_EDGE - (GRID_SIZE * 11))
    draw_digit(digits[1], down_turtle)
    wn.listen()    

def draw_to_go():
    score = wn.numinput("TO GO", "", default=1, minval=1, maxval=99)
    digits = parse_value(score)
    to_go_turtle.clearstamps()
    to_go_turtle.penup()
    to_go_turtle.setpos(LEFT_EDGE + (GRID_SIZE * 30), TOP_EDGE - (GRID_SIZE * 11))
    draw_digit(digits[0], to_go_turtle)
    draw_digit(digits[1], to_go_turtle)
    wn.listen()    

def draw_quarter():
    score = wn.numinput("QUARTER", "", default=1, minval=1, maxval=4)
    digits = parse_value(score)
    quarter_turtle.clearstamps()
    quarter_turtle.penup()
    quarter_turtle.setpos(LEFT_EDGE + (GRID_SIZE * 42), TOP_EDGE - (GRID_SIZE * 11))
    draw_digit(digits[1], quarter_turtle)
    wn.listen()    


draw_labels()

wn.onkey(draw_home, "h")
wn.onkey(draw_away, "a")
wn.onkey(draw_minutes, "m")
wn.onkey(draw_seconds, "s")
wn.onkey(draw_ball_on, "b")
wn.onkey(draw_down, "d")
wn.onkey(draw_to_go, "t")
wn.onkey(draw_quarter, "q")

wn.listen()
wn.mainloop()
