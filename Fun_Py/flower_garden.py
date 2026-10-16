import turtle
import math

s = turtle.Screen()
s.bgcolor("black")
s.setup(900, 900)

t = turtle.Turtle()
t.speed(0)
t.width(2)


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def flower(x, y, color, size=1):

    # Stem
    t.pencolor("#4d7c4d")
    move(0, -350)
    t.goto(x, y)

    # Flower petals
    t.pencolor(color)
    t.fillcolor(color)

    for a in range(0, 360, 30):
        move(x, y)
        t.setheading(a)

        t.begin_fill()

        for i in range(2):
            t.circle(28 * size, 60)
            t.left(120)

        t.end_fill()

    # Flower center
    move(x, y)
    t.dot(30 * size, "#ffd166")


flowers = [
    (-180, 30, "#ff4d6d", 1.1),
    (-90, 130, "#ff70a6", 1.2),
    (0, 180, "#e63946", 1.3),
    (100, 120, "#ff9f1c", 1.1),
    (190, 20, "#ffd60a", 1.2),
    (-80, -30, "#c77dff", 1),
    (85, -40, "#80ed99", 1)
]


for f in flowers:
    flower(*f)


turtle.done()
