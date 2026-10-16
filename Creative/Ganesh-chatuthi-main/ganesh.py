import cv2
import numpy as np
import turtle


image_path = 'ganesh.png'
img = cv2.imread(image_path)

if img is None:
    print("Error: 'ganesh.png' nahi mili! Check karein ki photo sahi folder me hai.")
    exit()

# Setup screen box to cover 80% of monitor screen
screen = turtle.Screen()
screen.setup(width=0.8, height=0.8)
screen.bgcolor("black")
screen.title("Python Color Sketch Drawing - Ganesh")
turtle.colormode(255)

# Dynamically scale sketch image size relative to window dimensions
window_w = screen.window_width()
window_h = screen.window_height()
draw_size = int(min(window_w, window_h) * 0.85)
width, height = draw_size, draw_size

img = cv2.resize(img, (width, height))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 60, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

t = turtle.Turtle()
t.speed(0)          
t.hideturtle()      
t.shape("classic")  
t.showturtle()
t.pensize(2)

# Fast animation speed (updates screen every 15 frames)
screen.tracer(15, 0)

print("Drawing start ho rahi hai...")

for cnt in contours:
    if len(cnt) < 8:  
        continue
        
    t.penup()
    first_pt = cnt[0][0]
    
    b, g, r = img[first_pt[1], first_pt[0]]
    
    if r < 40 and g < 40 and b < 40:
        t.pencolor(0, 200, 255)  # Cyan/Blue
    else:
        t.pencolor(min(int(r * 1.3), 255), min(int(g * 1.3), 255), min(int(b * 1.3), 255))
    
    start_x = first_pt[0] - width // 2
    start_y = height // 2 - first_pt[1]
    
    t.goto(start_x, start_y)
    t.pendown()
    
    for pt in cnt[1:]:
        x = pt[0][0] - width // 2
        y = height // 2 - pt[0][1]
        t.goto(x, y)

screen.update()
print("Drawing Complete!")
turtle.done()
