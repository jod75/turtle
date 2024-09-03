import turtle

# Create a turtle
star_turtle = turtle.Turtle()
star_turtle.color("red")

# Draw a star
for _ in range(5):
    star_turtle.forward(150)  # Move forward by 150 units
    star_turtle.right(144)    # Turn right by 144 degrees

# Keep the window open until clicked
turtle.done()
