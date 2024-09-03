import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=400, height=400) 
screen.bgcolor("black")  # Set the background color to black

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")  # Optional: Set the turtle's shape to 'turtle'
my_turtle.color("green")   # Set the turtle's color to green

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees

# Keep the window open until clicked
turtle.done()