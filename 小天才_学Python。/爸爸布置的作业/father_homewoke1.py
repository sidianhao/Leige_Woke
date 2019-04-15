# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 11:01
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : father_homewoke1.py
# @Software: PyCharm
name = input('你叫什么名字：')
Born_period = eval(input('你是那一年出生的:'))
while Born_period>2019:
    Born_period = eval(input('你输入的超过今年，请重新输入：'))
print("你好{},你现在是{}岁".format(name,(2019-Born_period)))