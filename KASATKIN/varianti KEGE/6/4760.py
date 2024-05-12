from turtle import *
color('black', 'red')
m = 100
speed(0)
begin_fill()
left(90)
for i in range(4):
    for k in range(3):
        forward(3 * m)
        right(90)
    left(180)
end_fill()
canvas = getcanvas()
cnt = 0
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x ,y)
        if len(item) == 1 and item[0] == 5:
            cnt += 1
print(cnt)
done()