from turtle import *
bgcolor("black")
color("orange")
speed(0)
for i in range(200):
    goto(0, 0)
    fd(250)
    lt(2)
    circle(150, -90)
    rt(90)
    hideturtle()
done()