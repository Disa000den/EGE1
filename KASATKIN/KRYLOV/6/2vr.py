from turtle import *
speed(1000)
m = 10
left(90)
down()
for i in range(2):
    forward(15 * m)
    left(90)
    forward(20 * m)
    left(90)
up()
right(90)
backward(7 * m)
left(90)
forward(9 * m)
down()
for k in range(2):
    forward(17 * m)
    right(90)
    forward(15 * m)
    right(90)
up()
for x in range(-20, 50):
    for y in range(-20, 50):
        goto(x * m, y * m)
        dot(3)
done()
