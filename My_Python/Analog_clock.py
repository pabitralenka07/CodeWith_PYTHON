import turtle
import time
import math

wn = turtle.Screen()
wn.title("Analog Clock")
wn.bgcolor("black")
wn.setup(width=500, height=500)

clock = turtle.Turtle()
clock.hideturtle()
clock.speed(0)
clock.pensize(3)


def draw_hand(angle, length, color, width):
    clock.color(color)
    clock.width(width)

    clock.penup()
    clock.goto(0, 0)

    clock.setheading(90 - angle)

    clock.pendown()
    clock.forward(length)
    clock.penup()


def draw_clock():
    clock.clear()

    clock.color("white")
    clock.penup()
    clock.goto(0, -200)
    clock.setheading(0)
    clock.pendown()
    clock.circle(200)
    clock.penup()

    now = time.localtime()

    sec = now.tm_sec
    minute = now.tm_min
    hour = now.tm_hour % 12

    sec_angle = sec * 6
    min_angle = minute * 6 + sec * 0.1
    hour_angle = hour * 30 + minute * 0.5

    draw_hand(sec_angle, 150, "red", 1)
    draw_hand(min_angle, 120, "green", 3)
    draw_hand(hour_angle, 80, "blue", 5)


while True:
    draw_clock()
    wn.update()
    time.sleep(1)

