import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
flower_turtle = turtle.Turtle()
flower_turtle.speed(0)
flower_turtle.pensize(5)
colors = ["red", "yellow", "blue", "green", "orange", "purple"]

# Draw a flower pattern
for angle in range(180):
    flower_turtle.color(colors[angle % 6])
    x = 100 * math.cos(math.radians(angle)) * math.sin(math.radians(angle * 5))
    y = 100 * math.sin(math.radians(angle)) * math.sin(math.radians(angle * 5))
    flower_turtle.goto(x, y)
    flower_turtle.forward(1)

# Hide the turtle and keep the window open
flower_turtle.hideturtle()
turtle.done()
