# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 16:57
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 晃眼睛的图案.py
# @Software: PyCharm
import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red","yellow","blue","green"]
for x in  range(200):
    t.pencolor(colors[x%4])
    turtle.bgcolor(colors[(x + 1)%4])
    t.forward(x)
    t.left(90)
turtle.done()