import turtle as t

t.speed(0)
t.bgcolor('black')
t.pencolor('orange')
def square(x, y):
    for j in range(4):
        t.forward(x)
        t.right(y)
for i in range(80):
    square(170, 90)
    t.right(5)
    t.circle(50)
    t.right(50)
    t.hideturtle()
t.done()