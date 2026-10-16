import math
from turtle import *

color("white")
penup()
goto(0, -50)
pendown()
style = ("adwa-assalaf", 50, "bold")
write("BABU", font=style, align="center")

def heart_a(n):
    return 15 * math.sin(n) ** 3

def heart_b(n):
    return 12 * math.cos(n)-5 *\
           math.cos(2*n) - 2 *\
            math.cos(3*n) - \
            math.cos(4*n)

speed(10)
bgcolor("black")
penup()
goto(0,60)
pendown()
for i in range(700):
    goto(heart_a(i)*20, heart_b(i)*20)
    for j in range(5):
            color('#f73487')
            hideturtle()

done()