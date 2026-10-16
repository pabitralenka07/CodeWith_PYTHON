from turtle import *
from colorsys import *
bgcolor("black")
tracer(100)
h = 0
b = "black"
for i in range(800):
    h+= 0.004
    color(hsv_to_rgb(h,1,1),b)
    goto(0, 0)
    begin_fill()
    fd(270)
    rt(2)
    circle(150,-90)
    end_fill()
    lt(90)
    hideturtle()
done()

