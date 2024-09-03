import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
mandala_turtle = turtle.Turtle()
mandala_turtle.speed(0)  # Set the turtle's speed to the fastest

colors = ["red", "blue", "green", "orange", "purple", "yellow"]

# Draw a mandala pattern
for i in range(36):
    mandala_turtle.color(colors[i % 6])  # Cycle through colors
    mandala_turtle.circle(100)           # Draw a circle with a radius of 100
    mandala_turtle.right(10)             # Turn right by 10 degrees

# Keep the window open until clicked
turtle.done()
