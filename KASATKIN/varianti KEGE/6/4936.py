from turtle import *
color('black', 'red')
speed(1000)
m = 15
begin_fill()
left(90)
for i in range(12):
    forward(8 * m)
    right(30)
end_fill()
for x in range(-30 * m, 30 * m):
    for y in range(-30 * m, 30 * m):
        goto(x, y)
        dot(3)
done()