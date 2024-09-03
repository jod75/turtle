import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
lissajous_turtle = turtle.Turtle()
lissajous_turtle.speed(0)
lissajous_turtle.color("white")

# Draw a Lissajous curve
for t in range(1000):
    x = 200 * math.sin(3 * math.radians(t))
    y = 200 * math.cos(2 * math.radians(t))
    lissajous_turtle.goto(x, y)

# Hide the turtle and keep the window open
lissajous_turtle.hideturtle()
turtle.done()
