# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 18:02
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 点餐程序.py
# @Software: PyCharm
num = 0  # 菜的总数
total = 0  # 菜的总价
name = input("请输入菜名：")
while name != "q":
    price = eval(input("请输入价格："))
    num = num + 1
    total = total + price
    name = input("请输入下一道菜：")
print("您一共点了", num, "道菜，总价为", total, "元")
