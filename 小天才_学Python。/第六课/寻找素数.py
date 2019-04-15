# -*- coding: utf-8 -*-
# @Time    : 2019/4/14  0:06
# @Author  : 史哲磊
# @Email   : sidian305@163.com
# @File    : 寻找素数
# @Software: PyCharm
for i in range(2,100):
    flag=True
    for j in range(2,i):
        if i//j==i/j:
            flag=False
            break
    if(flag):
        print("{}是素数。".format(i))