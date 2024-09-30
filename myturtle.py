import turtle

screen = turtle.Screen()
screen.bgcolor("#00254d")

my_turtle = turtle.Turtle()
my_turtle.color("white")
my_turtle.shape("turtle")
my_turtle.speed(0.25)

def move_pen(x, y):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

def draw_circle( x, y, r):
    move_pen(x, y)
    my_turtle.circle(r)
    
def draw_line( x1, y1, x2, y2):
    my_turtle.penup()
    my_turtle.goto(x1, y1)
    my_turtle.pendown()
    my_turtle.goto(x2, y2) 
    
def draw_shell(turt: turtle.Turtle):   
    turt.rt(36)
    
    for i in range(5):
        turt.fd(60)
        turt.rt(360 // 5)
        
    draw_line(0, 50, 0, 100)
    draw_line(50, 15, 90, 40)
    draw_line(-50, 15, -90, 40)
    draw_line(30, -40, 70, -70)
    draw_line(-30, -40, -70, -70)


# Body
draw_circle(0, -100, 100)

# Head 
draw_circle(0, 100, 40)

# Hands
draw_circle(-100, 40, 20) # Left hand
draw_circle(100, 40, 20) # Right hand

# Feet
draw_circle(-80, -100, 15) # Left foot
draw_circle(80, -100, 15) # Right foot
    
# Tail 
draw_line(10, -100, 0, -120) 
draw_line(0, -120, -10, -100) 

# Shell
move_pen(0, 50), # Move to the correct shell position
draw_shell(my_turtle)

# Eyes
draw_circle(-15, 160, 5)
draw_circle(10, 160, 5)

my_turtle.hideturtle() 

turtle.done()