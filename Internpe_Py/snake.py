import tkinter as tk
import random

# Constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])
            square = canvas.create_rectangle(0, 0, SPACE_SIZE, SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    # Move the snake and check for collisions
    # Update the canvas and call next_turn again
    pass

def change_direction(new_direction):
    # Change the direction of the snake
    pass

def check_collisions(snake):
    # Check for collisions with walls or itself
    pass

def game_over():
    # Display game over message
    pass

# Setup the window
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

score = 0
direction = "down"

# Create snake and food objects
snake = Snake()
food = Food()

# Bind keys
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

window.mainloop()