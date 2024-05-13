from turtle import *
color('black', 'red')
m = 100
speed(1000)
begin_fill()
left(90)
right(45)
for i in range(2):
    forward(5 * m)
    right(45)
    forward(10 * m)
    right(135)
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