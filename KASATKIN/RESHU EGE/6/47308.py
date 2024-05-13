import turtle as t
k = 20
t.speed(20)
for i in range(1, 6):
    t.forward(8 * k)
    t.right(60)
    t.forward(8 * k)
    t.right(120)
t.up()
t.speed(20)
for x in range(20, -20, -1):
    for y in range(20, -20, -1):
        t.goto(x * k, y * k)
        t.dot(4)
t.done()