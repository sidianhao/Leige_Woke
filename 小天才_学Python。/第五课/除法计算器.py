# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 17:20
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 除法计算器.py
# @Software: PyCharm
a = eval(input('a='))
b = eval(input('b='))
if a==0:
    print('出错啦！a不能为0！')
if b==0:
    print('出错啦！b不能为0！')
else:
    print('a/b=',a/b)