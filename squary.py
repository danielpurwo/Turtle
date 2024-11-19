import turtle

# Set up the screen and turtle
turtle.speed(0)  # Maximum speed for smooth animation
turtle.bgcolor('black')  # Set background color
h = 0.0
colors = ['royalblue', 'aqua']  # Define the colors

turtle.penup()  # Lift the pen to move without drawing
turtle.goto(0, 225)  # Go to the starting position
turtle.pendown()  # Put the pen down to start drawing

# Drawing loop
for i in range(400):
    turtle.forward(i + 200)
    turtle.right(189)  # Rotate right by 189 degrees
    turtle.left(100)  # Rotate left by 100 degrees
    turtle.forward(120)
    turtle.pencolor(colors[i % 2])  # Alternate pen colors

turtle.done()