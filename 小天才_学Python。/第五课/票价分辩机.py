# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 17:29
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 票价分辩机.py
# @Software: PyCharm
print('欢迎你来购买机票！')
age = eval(input('请告诉我你的年龄：'))
if age<12:
    print('你可以购买儿童票。')
else:
    print('你需要购买全价票。')