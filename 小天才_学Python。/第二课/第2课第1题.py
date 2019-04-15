# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 17:35
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 第2课第1题.py
# @Software: PyCharm
import turtle
t = turtle.Pen()
t.speed(0)
for x in range(200):
    t.circle(x)
    t.left(90)
turtle.done()