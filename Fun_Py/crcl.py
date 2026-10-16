from turtle import *
setpos (40, 50)
speed(0)
bgcolor('black')
for i in range(40):
    color('yellow')
    for j in range(4):
        circle(40+j*4,  -90)
        fd(300)
        rt(90)
        circle(10)
        rt(10)
        done()