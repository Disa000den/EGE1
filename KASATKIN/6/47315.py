from turtle import *
color('black', 'red')
m = 100
speed(1000)
begin_fill()
left(90)
for i in range(2):
    forward(7 * m)
    right(90)
    forward(7 * m)
    right(90)
end_fill()
canvas = getcanvas()
cnt = 0
for y in range(-100 * m, 100 * m, m):
    for x in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) >= 1:
            cnt += 1
print(cnt)
done()
#так как в задании написано, что точки на границе учитывать стоит, то убираем len(item) == 1 and item[0] == 5
# и пишем только len(item) >= 1