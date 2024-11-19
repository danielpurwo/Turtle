import turtle
import colorsys
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Accurate Flower of Life with Gradient")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)  # Max speed
pen.hideturtle()
pen.width(2)

# Parameters
radius = 80  # Radius of each circle
layers = 3  # Number of layers (central + 2)
hue_start = 0.0  # Starting hue for gradient

# Function to draw a circle
def draw_circle(x, y, r, color):
    pen.penup()
    pen.goto(x, y - r)  # Move to the top of the circle
    pen.pendown()
    pen.pencolor(color)
    pen.circle(r)

# Function to convert HSV to RGB for colors
def hsv_to_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*186):02x}"

# Draw the Flower of Life pattern
def draw_flower_of_life():
    saturation, brightness = 1, 1  # Full saturation and brightness

    # Central circle
    hue = hue_start
    draw_circle(0, 0, radius, hsv_to_rgb(hue, saturation, brightness))
    hue += 0.05  # Increment hue for gradient effect

    # Draw surrounding layers
    for layer in range(1, layers + 1):
        num_circles = 8 * layer  # Number of circles in the current layer
        angle_step = 360 / num_circles  # Angle between adjacent circles

        for i in range(num_circles):
            angle = i * angle_step
            # Calculate circle center
            x = layer * radius * math.cos(math.radians(angle))
            y = layer * radius * math.sin(math.radians(angle))
            # Calculate color based on position
            color = hsv_to_rgb((hue + i * 0.02) % 1.0, saturation, brightness)
            # Draw circle
            draw_circle(x, y, radius, color)
        # Adjust hue for the next layer
        hue += 0.1 

# Run the drawing
draw_flower_of_life()

# Complete
turtle.done()
