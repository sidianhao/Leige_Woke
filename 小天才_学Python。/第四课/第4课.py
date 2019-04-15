# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 17:15
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 第4课.py
# @Software: PyCharm
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = 8
t.speed(0)
colors = ["red","yellow","blue","orange","green","purple","pink","white"]
for x in  range(270):
    t.pencolor(colors[x%sides])
    t.forward(x*2)
    t.left(360/sides+1)
    t.width(x*sides/150)
turtle.done()