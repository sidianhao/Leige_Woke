# -*- coding: utf-8 -*-
# @Time    : 2019/4/13  21:58
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 九九乘法表（自制）
# @Software: PyCharm
for x in range(1,10):
    for j in range(1,x+1):
        print(j,end="")
        print("*",end="")
        print(x,end="")
        print("=",end="")
        print(x*j,end="\t")
    print()