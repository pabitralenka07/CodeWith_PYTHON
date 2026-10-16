import turtle

# Setup the turtle window
screen = turtle.Screen()
screen.title("Indian Flag")
screen.setup(width=400, height=200)
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(10)

# Function to draw a rectangle (for flag stripes)
def draw_rectangle(color, width, height):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()    
# Function to draw the Ashoka Chakra
def draw_ashoka_chakra(radius):
    t.penup()
    t.goto(0, 1)  # Position to center the Chakra in the white stripe
    t.pendown()
    t.color("navy")
    t.circle(radius)  # Outer circle

    # Draw 24 spokes
    for _ in range(24):
        t.penup()
        t.goto(0, 50)
        t.pendown()
        t.forward(radius)
        t.backward(radius)
        t.right(15)  # Angle between spokes

# Draw the flag with corrected alignment
t.penup()
t.goto(-200, 200)  # Start position (top left corner for saffron stripe)
t.pendown()

# Draw Saffron rectangle (top stripe)
draw_rectangle("orange", 400, 100)

# Move to next stripe (white)
t.right(90)
t.forward(100)
t.left(90)

# Draw White rectangle (middle stripe)
#draw_rectangle("white", 400, 100)
#draw_ashoka_chakra(50)

# Move to next stripe (green)
#t.right(90)
#t.forward(50)
#t.left(90)

# Draw Green rectangle (bottom stripe)
draw_rectangle("white", 400, 100)

t.right(90)
t.forward(100)
t.left(90)

# Draw White rectangle (middle stripe)
draw_rectangle("green", 400, 100)
draw_ashoka_chakra(50)

# Move to next stripe (green)
t.right(90)
t.forward(50)
t.left(90)




# Hide the turtle and finish
#t.hideturtle()
turtle.done()
