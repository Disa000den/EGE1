from turtle import *
m = 10
speed(1000)
left(90)
for i in range(2):
    forward(17 * m)
    left(90)
    forward(10 * m)
    left(90)
up()
backward(4 * m)
right(90)
backward(3 * m)
left(90)
down()
for k in range(2):
    forward(40 * m)
    right(90)
    forward(10 * m)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 40):
        goto(x * m, y * m)
        dot(3)
done()
