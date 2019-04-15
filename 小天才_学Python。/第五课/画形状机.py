# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 17:39
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 画形状机.py
# @Software: PyCharm
import turtle
t = turtle.Pen()
choice = input('请选择：1.三角形2.圆形3.正方形：')
if choice=='1':
    t.forward(90)
    t.left(120)
    turtle.done()
elif choice=='2':
        t.circle(90)
        turtle.done()

elif choice=='3':
         for x in  range(4):
             t.forward(90)
             t.left(90)
         turtle.done()
else:
     print('出错啦！只能输入1~3。')
