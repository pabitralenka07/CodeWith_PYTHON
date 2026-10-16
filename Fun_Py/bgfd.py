from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h = 0
for i in range(75):
    h += 0.0016
    color(hsv_to_rgb(h, 1, 1))
    lt(50)
    for j in range(5):
        fd(280)
        lt(145)
    hideturtle()
done()