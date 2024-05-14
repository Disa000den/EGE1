from turtle import *
m = 10
speed(1000)
left(90)
for i in range(3):
    down()
    for k in range(2):
        forward(10 * m)
        right(90)
        forward(10 * m)
        right(90)
    up()
    forward(10 * m)
    right(90)
    forward(5 * m)
    left(90)
for x in range(-20, 30):
    for y in range(-20, 40):
        goto(x * m, y * m)
        dot(3)
done()