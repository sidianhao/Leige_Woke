# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 10:00
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 猜数字游戏（自制）.py
# @Software: PyCharm
import random
print('欢迎来到猜数字游戏。')
j = random.randint(1,10)
number = eval(input('猜猜这个数字是什么?(1~100)有十次机会：'))
d = 10
if_is = 1
while d>1:
    if number>j:
        number = eval(input('你猜的太大了,还剩下{}次请重新猜：'.format(d-1)))
        d = d-1
    if number<j:
        number = eval(input('你猜的太小了,还剩下{}次请重新猜：'.format(d-1)))
        d = d - 1
    if number==j:
        print('恭喜你猜中了，你一共猜了%s次。'% (11-d))
        if_is = 0
        break

if if_is:
    print("你猜的次数已经用光了，答案是",j,"下次加油哦。")