from turtle import *
from random import *

setposition(0,-250)
tracer(100)
bgcolor("black")
color("#975200")
shape("turtle")
left(90)

def tree(length):
    rand = (random()-0.5)*4
    realLength =length+rand
    width(length/10)
    fd(realLength)

    if length >10:
        color("#975200")
        left(30)
        tree(3*realLength/4)
        left(-30)

    if length > 10:
        color("#975200")
        left(-30)
        tree(3*realLength/4)
        left(30)
    fd(-realLength)
    color("green")
    circle(2)
    hideturtle()

clear()
tree(130)
done()
