# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 16:41
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 复杂的正方形（彩色）.py
# @Software: PyCharm
import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red","yellow","blue","green"]
for x in  range(200):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(90)
turtle.done()