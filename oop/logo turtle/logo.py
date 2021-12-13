import turtle

STANDARD_LOGO_SIZE = 256
text_list = []

def draw_logo(x, y, scale = 1, angle = 0):
    
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(0)
    
    turtle_obj.penup()

    turtle_obj.goto(x, y)
    turtle_obj.setheading(angle)

    turtle_obj.forward(STANDARD_LOGO_SIZE * scale * 0.5)

    turtle_obj.pendown()

    turtle_obj.fillcolor('black')
    turtle_obj.begin_fill()
    turtle_obj.pencolor('white')
    turtle_obj.pensize(10)
    turtle_obj.circle((STANDARD_LOGO_SIZE * 0.5) * scale * -1)

    turtle_obj.end_fill()

    turtle_obj.pencolor('black')
    turtle_obj.pensize(2)
    turtle_obj.circle((STANDARD_LOGO_SIZE * 0.5) * scale * -1)


    #starts inner part of logo
    turtle_obj.penup()
    turtle_obj.right(90)
    turtle_obj.forward(STANDARD_LOGO_SIZE * scale * 0.175)

    turtle_obj.begin_fill()
    turtle_obj.fillcolor('white')
    turtle_obj.pendown()
    turtle_obj.left(90)
    turtle_obj.circle((STANDARD_LOGO_SIZE * 0.325) * scale * -1)

    turtle_obj.end_fill()
    turtle_obj.penup()
    #inner part of bmw logo
    turtle_obj.pensize(3)
    turtle_obj.left(90)
    turtle_obj.forward(STANDARD_LOGO_SIZE * scale * 0.175)
    turtle_obj.right(180)
    turtle_obj.forward(STANDARD_LOGO_SIZE * scale * 0.5)

    turtle_obj.pendown()
    turtle_obj.fillcolor("blue")
    turtle_obj.begin_fill()
    turtle_obj.forward(STANDARD_LOGO_SIZE * scale * 0.325)

    turtle_obj.left(90)

    
    turtle_obj.circle((STANDARD_LOGO_SIZE * 0.325) * scale,90)

    

    turtle_obj.left(90)
    turtle_obj.forward(STANDARD_LOGO_SIZE * scale * 0.325)

    turtle_obj.end_fill()

    turtle_obj.begin_fill()
    turtle_obj.forward(STANDARD_LOGO_SIZE * scale * 0.325)
    turtle_obj.right(90)
    turtle_obj.circle((STANDARD_LOGO_SIZE * 0.325) * scale * -1,90)
    turtle_obj.right(90)
    turtle_obj.forward(STANDARD_LOGO_SIZE * scale * 0.325)
    turtle_obj.end_fill()


    #draws the text
    turtle_obj.penup()
    turtle_obj.color('white')
    
    

    turtle_obj.right(180)
    turtle_obj.forward(STANDARD_LOGO_SIZE * scale * 0.35)

    width, height = turtle.screensize()
    x,y = turtle_obj.pos()

    canvas = turtle.getcanvas()

    print(x,y)


    tk_abs_x = x + (width / 2)
    tk_abs_y = ((y * -1) + (height / 2))

    text_list.append(canvas.create_text(tk_abs_x, tk_abs_y, text='M', angle=angle, font=("Arial", 30, "normal")))

    



if __name__ == "__main__":
    import tkinter 

    print(tkinter.TkVersion)
    draw_logo(0,0,angle=90)

    input()