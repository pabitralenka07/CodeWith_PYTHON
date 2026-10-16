import random
from turtle import *
setup(600,600)
setworldcoordinates(-6,-1,5,11)
tracer(0)
bgcolor("black")
up()
n=100000
p=(0,0)
up()
hideturtle()
for i in range(n):
    goto(p)
    dot(2,'#00AF00')
    r=random.uniform(0,1)
    if r<0.01:
        p = (0,0.16*p[1])
    elif r<0.86:
        p=(0.85*p[0]+0.04*p[1],
            -0.04*p[0]+0.85*p[1]+1.6)
    elif r<0.93:
        p=(0.2*p[0]-0.26*p[1],
            0.23*p[0]+0.22*p[1]+1.6)
    else:
        p=(-0.15*p[0]+0.28*p[1],
            0.26*p[0]+0.24*p[1]+0.44)
    if i%1000 == 0:
        Turtle()
        up()
        update()
done()