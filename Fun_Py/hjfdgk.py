from turtle import *
from colorsys import *
tracer(10)
bgcolor("black")
h = 0
pensize(2)
for i in range(270):
    h += 0.0015
    color(hsv_to_rgb(h, 1, 1))
    up()
    fd(i/2)
    goto(0, 0)
    down()
    rt(60)
    fillcolor("black")
    begin_fill()
    circle(-i, 60)
    end_fill()
    rt(144)
    for j in range(3):
        circle(j*10, 90)
        rt(105)
    hideturtle()
done()