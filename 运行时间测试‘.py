import time
def calcProd():
    num = 1
    for i in range(1,5000):
        num = num * i
    return num

s_time = time.time()
getnum = calcProd()
e_time = time.time()
print('这个数字%d位。' % len(str(getnum)))
print('这个数字是%s。' % getnum)
print('程序运行时间一共花了%s秒。' % round((e_time-s_time)))


print(round(3.66666,2))
