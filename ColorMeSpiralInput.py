import turtle,time
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "grey"]
for x in range(100):
    t.pencolor(colors[x % 8])
    t.forward(x)

    t.left(180)
turtle.done()
