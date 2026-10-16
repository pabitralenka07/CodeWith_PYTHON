from turtle import *
import colorsys
speed(0)
bgcolor("black")
pensize(2)
R = 0
for i in range(122):
    color(colorsys.hsv_to_rgb(R, 1, 1))
    R += 0.010
    rt(70)
    fd(i)
    circle(i, -10)
    lt(100)
    up()
    fd(i)
    down()
    circle(i * 2, -90)
    hideturtle()

done()