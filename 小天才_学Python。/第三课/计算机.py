# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 17:51
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 计算机.py
# @Software: PyCharm
question = input('请输入一道计算题：')
while question != "q":
    print(question,"的答案是：",eval(question))
    question = input('请输入下一个题目，按“q”退出')