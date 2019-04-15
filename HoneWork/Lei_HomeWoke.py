# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 14:26
# @Author  : Sidian
# @Email   : sidian305@163.com
# @File    : Lei_HomeWoke.py
# @Software: PyCharm
import datetime,pickle


def initialize(mes_in_0):
    global subject_list, subject_dict, wk, sum_no, sum_yes, k, v
    subject_list = ['语文', '数学', '英语', '科学', '体育', '额外作业']
    subject_dict = {i: [[], []] for i in subject_list}
    if mes_in_0 == 'r':
        with open('wk.txt', 'rb') as wk:
            subject_dict = pickle.load(wk)
    elif mes_in_0 == 'n':
        time = str(datetime.datetime.now())
        newtime = time.split('.')
        newtime = newtime[0]
        with open('wk.txt', 'rb') as wk:
            subject_dict = pickle.load(wk)
        with open('作业记录.txt', 'a') as f:
            sum_no = 0
            sum_yes = 0
            for k, v in subject_dict.items():
                f.write('科目({}):已完成作业{},未完成作业{}。\n'.format(k, v[1], v[0]))
                sum_no += len(v[0])
                sum_yes += len(v[1])
            f.write('在{}之前记录下你已经完成作业{}项，还剩下{}项未完成。\n \n \n \n'.format(newtime, sum_yes, sum_no))
        subject_dict = {i: [[], []] for i in subject_list}
    else:
        print('你输入的内容有误，已经按照默认读取最近一次作业情况！')
        with open('wk.txt', 'rb') as wk:
            subject_dict = pickle.load(wk)


def add_work():
    global mes_in_2, mes_in_3, subject
    while True:
        mes_in_2 = int(mes_in_2)
        print('请输入该({})科目作业，每次输一条，按“q”键返回:'.format(subject_list[mes_in_2 - 1]), end='')
        mes_in_3 = input('')
        if mes_in_3 != 'q' and mes_in_3 != '':
            subject = subject_list[mes_in_2 - 1]
            subject_dict[subject][0].append(mes_in_3)
        elif mes_in_3 == '':
            print('你未输入作业内容，请重新核实后输入。')
        else:
            break


def del_work():
    global mes_in_2, i, mes_in_4
    while True:
        mes_in_2 = int(mes_in_2)
        print('该({})科目作业如下，请输入你需要删除的编号，按“q”键返回:'.format(subject_list[mes_in_2 - 1]))
        for i in enumerate(subject_dict[subject_list[mes_in_2 - 1]][0], 1):
            print(i)
        mes_in_4 = input('')
        if mes_in_4.isnumeric():
            if int(mes_in_4) in range(1, len(subject_dict[subject_list[mes_in_2 - 1]][0]) + 1):
                print('({})的作业已经删除'.format(subject_dict[subject_list[mes_in_2 - 1]][0][int(mes_in_4) - 1]))
                del subject_dict[subject_list[mes_in_2 - 1]][0][int(mes_in_4) - 1]
                break
        else:
            print('输入有误，返回上一层')
            break



def change_work():
    global mes_in_2, i, mes_in_4
    while True:
        mes_in_2 = int(mes_in_2)
        print('该({})科目未作业如下，如已完成输入序号，按“q”键返回:'.format(subject_list[mes_in_2 - 1]))
        for i in enumerate(subject_dict[subject_list[mes_in_2 - 1]][0], 1):
            print(i)
        mes_in_4 = input('')
        if mes_in_4.isnumeric():
            if int(mes_in_4) in range(1, len(subject_dict[subject_list[mes_in_2 - 1]][0]) + 1):
                print('({})的作业已完成，感谢你的努力，你的配合'.
                      format(subject_dict[subject_list[mes_in_2 - 1]][0][int(mes_in_4) - 1]))
                subject_dict[subject_list[mes_in_2 - 1]][1]. \
                    append(subject_dict[subject_list[mes_in_2 - 1]][0].pop(int(mes_in_4) - 1))
        else:
            print('输入有误，返回上一层')
            break


if '__main__' == __name__:
    print('欢迎进入磊磊小学作业管理系统'.center(50, '*'))
    print('读取最近一次作业情况请按“r，重新新建作业文档请按"n"：', end='')
    mes_in_0 = input('')
    initialize(mes_in_0)   #初始化作业
    while True:
        print('#' * 50)
        print('#      添加作业按"a"        删除作业按"d"          #')
        print('#                                                #')
        print('#      完成作业按"c"        查询作业按"s"          #')
        print('#                                                #')
        print('#                退出请按"q"：                    #')
        print('#' * 50)
        mes_in_1 = input('输入:')
        if mes_in_1.lower() == 'a':     #增加作业
            while True:
                print('请操作你需要添加作业的序号,退出请按“q”')
                for i in enumerate(subject_dict,1):
                    print(i)
                mes_in_2 = input('请输入：')
                if mes_in_2 == '1':
                    add_work()
                elif mes_in_2 == '2':
                    add_work()
                elif mes_in_2 == '3':
                    add_work()
                elif mes_in_2 == '4':
                    add_work()
                elif mes_in_2 == '5':
                    add_work()
                elif mes_in_2 == '6':
                    add_work()
                elif mes_in_2 == 'q':
                    break
                else:
                    print('输入无效，请重新输入。')
        elif mes_in_1 == 'd':
            while True:
                print('请操作你需要删除作业的科目序号,退出请按“q”')
                for i in enumerate(subject_dict,1):
                    print(i)
                mes_in_2 = input('请输入：')
                if mes_in_2 == '1':
                    del_work()
                elif mes_in_2 == '2':
                    del_work()
                elif mes_in_2 == '3':
                    del_work()
                elif mes_in_2 == '4':
                    del_work()
                elif mes_in_2 == '5':
                    del_work()
                elif mes_in_2 == '5':
                    del_work()
                elif mes_in_2 == '6':
                    del_work()
                elif mes_in_2 == 'q':
                    break
                else:
                    print('输入无效，请重新输入。')
        elif mes_in_1 == 'c':
            while True:
                print('请操作你已完成作业的科目序号,退出请按“q”')
                for i in enumerate(subject_dict,1):
                    print(i)
                mes_in_2 = input('请输入：')
                if mes_in_2 == '1':
                    change_work()
                elif mes_in_2 == '2':
                    change_work()
                elif mes_in_2 == '3':
                    change_work()
                elif mes_in_2 == '4':
                    change_work()
                elif mes_in_2 == '5':
                    change_work()
                elif mes_in_2 == '6':
                    change_work()
                elif mes_in_2 == 'q':
                    break
                else:
                    print('输入无效，请重新输入。')
        elif mes_in_1 == 's':
            while True:
                sum_no = 0
                sum_yes = 0
                # print(subject_dict)
                for k,v in subject_dict.items():
                    # print('科目({}):已完成作业{},未完成作业{}。'.format(k,v[1],v[0]))
                    if len(v[1]):
                        print('科目({})已完成:'.format(k),end='')
                        for i in enumerate(v[1],1):
                            print(i,end='\t')
                        print()
                    if len(v[0]):
                        print('科目({})未完成:'.format(k),end='')
                        for i in enumerate(v[0],1):
                            print(i,end='\t')
                        print()
                    print('-'*100)
                    sum_no += len(v[0])
                    sum_yes += len(v[1])
                # print('截止到现在你已经完成作业{}项，还剩下{}项未完成。'.format(sum_yes,sum_no))
                mes_in_3 = input('截止到现在你已经完成作业{}项，还剩下{}项未完成,按任意键退出'.format(sum_yes,sum_no))
                print()
                if mes_in_3:
                    break
        elif mes_in_1 == 'q':
            print("已经退出，并保存作业情况.")
            with open('wk.txt','wb') as wk:
                pickle.dump(subject_dict,wk)
            break
        else:
            print('你输入的信息有误。')