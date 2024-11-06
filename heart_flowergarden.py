import turtle
import math

# Setup the screen
turtle.speed(10)
turtle.bgcolor("black")

#draw a flower
def draw_flower(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)

    #flower petals
    for _ in range(6):
        turtle.begin_fill()
        turtle.circle(30, 60)
        turtle.left(120)
        turtle.circle(30, 60)
        turtle.left(120)
        turtle.end_fill()
        turtle.left(60)

    #flower pollen
    turtle.penup()
    turtle.goto(x + 5, y) 
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

#plant stem
def draw_stem(x, y, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("green")
    turtle.setheading(90)
    turtle.pensize(5)
    turtle.forward(height)

# values in the garden of flowers
plants = [
    (-100, -275, 100, "red"),
    (-160, -285, 100, "pink"),
    (100, -275, 100, "blue"),
    (120, -275, 50, "violet"),
    (-130, -275, 60, "orange"),
    (-210, -285, 120, "grey"),
    (165, -260, 120, "white"),
    (190, -275, 80, "purple"),
    ]
    
for x, y, height, flower_color in plants:
    draw_stem(x, y, height)  # Draw plant stem
    draw_flower(x, y + height, flower_color)  # Draw plant flower

#ily msg
def draw_message():
    turtle.color("green")
    turtle.penup()
    turtle.goto(0, -275)
    turtle.pendown()
    turtle.hideturtle()
    turtle.write("I love you!", font=("Arial", 24, "bold"), align="center")

#Heart drawing
def heartA(k):
    return 15 * math.sin(k) ** 3

def heartB(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

def draw_heart(color_choice, scale):
    turtle.color(color_choice)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    for i in range(360):
        x = heartA(i * math.pi / 180) * scale
        y = heartB(i * math.pi / 180) * scale
        turtle.goto(x, y)
    turtle.end_fill()

#draw heart
def draw_hearts():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    draw_heart("red", 15) 

# Main function to control the drawings
def main():
    
    draw_message()
    turtle.ontimer(draw_hearts, 100)

# Start main 
main()
turtle.done()
