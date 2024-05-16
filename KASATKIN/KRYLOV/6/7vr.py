from turtle import *
color('black', 'red')
m = 100
speed(1000)
left(90)
up()
right(30)
begin_fill()
down()
for i in range(2):
    forward(30 * m)
    right(90)
    forward(40 * m)
    right(90)
end_fill()
canvas = getcanvas()
cnt = 0
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 * m, m):
       item = canvas.find_overlapping(x, y, x, y)
       if len(item) == 1 and item[0] == 5:
           cnt += 1
print(cnt)
done()