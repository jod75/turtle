import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
spirograph_turtle = turtle.Turtle()
spirograph_turtle.speed(0)
spirograph_turtle.color("lime")

# Parameters for the hypotrochoid
R = 100  # Radius of the fixed circle
r = 30   # Radius of the rolling circle
d = 60   # Distance from the center of the rolling circle

# Draw a hypotrochoid (spirograph)
for t in range(1100):
    x = (R - r) * math.cos(math.radians(t)) + d * math.cos((R - r) / r * math.radians(t))
    y = (R - r) * math.sin(math.radians(t)) - d * math.sin((R - r) / r * math.radians(t))
    spirograph_turtle.goto(x, y)

# Hide the turtle and keep the window open
spirograph_turtle.hideturtle()
turtle.done()
