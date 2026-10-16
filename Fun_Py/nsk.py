from turtle import *
from colorsys import *
tracer(200)
bgcolor("black")
h = 0
for i in range(40):
    fillcolor(hsv_to_rgb(h,1, 1))
    h += 0.5
    goto(0, 0)
    begin_fill()
    rt(50)
    circle(i, 12)
    fd(50)
    fd(i)
    lt(29)
    for j in range(129):
        fd(i)
        circle(j, 299, steps=2)
    end_fill()
done()
