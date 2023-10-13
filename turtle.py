import turtle
import colorsys

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)

# Function to draw a colorful spiral pattern
def draw_spiral():
    for i in range(360):
        hue = i / 360.0
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        spiral.pencolor(color)
        spiral.forward(i)
        spiral.right(59)

# Hide the turtle and display the pattern
spiral.hideturtle()
draw_spiral()

# Close the window on click
screen.exitonclick()
