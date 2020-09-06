import turtle

t = turtle.Turtle()
t.pensize(5)
t.speed(10)


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


t.color("blue")
for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)

move(0, -80)
t.circle(80, 360)

t.color("green")
t.begin_fill()
t.forward(350)
t.backward(700)
t.right(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.end_fill()

t.color("orange")
move(-350, 80)
t.begin_fill()
t.right(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.end_fill()

turtle.Screen().exitonclick()
