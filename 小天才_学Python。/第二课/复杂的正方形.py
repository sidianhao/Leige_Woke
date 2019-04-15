# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 17:27
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 复杂的正方形.py
# @Software: PyCharm
import turtle
t = turtle.Pen()
t.speed(0)
for x in range(200):
    t.forward(x)
    t.left(90)
turtle.done()