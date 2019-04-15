# SquareSpirall.py - Draws asquare spiral
import turtle,time
t = turtle.Pen()
t.speed(0)
for x in range(0,1000000000):
    t.forward(x)
    t.left(121)
turtle.done()