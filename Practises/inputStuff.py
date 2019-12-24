#!/usr/bin/env python
# -*- coding :utf-8 -*-
#author:shirenxiang time:2019/12/24 17:55
# name=input("请输入姓名")
# age=input("请输入年龄")
#
# # print("我叫"+name,"今年"+age +"了")
# print("我叫{}，今年{}了".format(name,age))

# print("{:.2f}".format(3.1415926))

#
# for i in range(1,10):
#     print('阿勇走的第{}天，想他想他'.format(i))

# a=1
# while a<10:
#     a=a+1
#     if a==3:
#         # break
#         continue
#     print(a)
# 逢7跳过
a=1
while a<101:
    if a%7==0:
        pass
    elif a%10==7:
        pass
    elif a//10==7:
        pass
        a=a+1
        continue
    else:
        print(a,end=" ")
    a=a+1