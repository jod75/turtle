import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
sine_wave_turtle = turtle.Turtle()
sine_wave_turtle.speed(0)
sine_wave_turtle.color("cyan")

# Draw a sine wave
for x in range(360):
    y = 100 * math.sin(math.radians(x))
    sine_wave_turtle.goto(x - 180, y)

# Hide the turtle and keep the window open
sine_wave_turtle.hideturtle()
turtle.done()
