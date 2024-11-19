import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Complex Motion Pattern with Gradient Effect")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Parameters for the gradient and pattern
num_of_colors = 360  # Total number of colors in the gradient
hue = 0  # Starting hue
num_of_steps = 300  # Total number of steps in the motion

# Function to convert HSV to RGB
def hsv_to_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

# Drawing the pattern
for i in range(num_of_steps):
    # Update the color gradient
    r, g, b = hsv_to_rgb(hue, 1, 1)
    pen.pencolor(r / 255, g / 255, b / 255)  # Set color in RGB format

    # Draw the pattern
    pen.forward(i * 2)
    pen.right(59)  # Change angle for complexity
    pen.left(5)    # Add an additional rotation for more motion effects

    # Update hue for gradient
    hue += 1 / num_of_colors
    if hue > 1:  # Loop hue back to 0 when it exceeds 1
        hue -= 1

# Finish
turtle.done()
