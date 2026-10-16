import turtle

# Function to draw a flower using turtle
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")
    
    # Create turtle object
    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.color("purple")
    flower.speed(50)
    
    # Draw a flower with 36 petals
    for _ in range(36):
        # Draw a petal
        for _ in range(2):
            flower.circle(100, 60)  # Draw half circle (petal)
            flower.left(120)        # Angle for the next half circle
            flower.circle(100, 60)
            flower.left(120)
        flower.right(10)  # Angle for next petal
        
    # Move turtle to the center and draw the stem
    flower.right(90)
    flower.forward(300)

    window.exitonclick()

# Call the function to draw the flower
draw_flower()