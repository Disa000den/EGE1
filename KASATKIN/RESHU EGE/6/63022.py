from turtle import *
color('black', 'red')
m = 25
speed(1000)
# begin_fill()
left(90)
for i in range(4):
    forward(14*m)
    right(90)
for k in range(5):
    forward(5 * m)
    right(45)
# end_fill()
# canvas = getcanvas()
cnt = 0
up()
for y in range(-10 * m, 100 * m, m):
    for x in range(-10 * m, 30 * m, m):
        # item = canvas.find_overlapping(x, y, x, y)
        # if len(item) == 1 and item[0] == 5:
        #     cnt +=1
        goto(x, y)
        dot(3)
print(cnt)
done()
#в этом задании нужно считать кол-во точек на линии фигур, а не внутри фигуры