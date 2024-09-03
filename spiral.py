import turtle

# Create a turtle
spiral_turtle = turtle.Turtle()
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Draw a spiral
for i in range(100):
    spiral_turtle.color(colors[i % 6])  # Cycle through colors
    spiral_turtle.forward(i * 5)        # Increase the length of each segment
    spiral_turtle.right(144)            # Turn right by 144 degrees

# Keep the window open until clicked
turtle.done()
