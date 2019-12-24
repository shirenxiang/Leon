#!/usr/bin/env python
# -*- coding :utf-8 -*-
#author:shirenxiang time:2019/12/24 17:56
'''第一个python程序'''
"""第一个python程序"""
# 这是石仁祥的python练习



import sys
str='shirenxiang'
print(str)
print(str[0:-1])
print(str*3)
print('shiren\nxiang')
print(r'shiren\nxiang')
print("我是",end="")
print("好人")

for i in sys.argv:
    print(i)
print('\n path路径为',sys.path)

def a():
    '''这是文档字符串'''
    pass
print(a.__doc__)

a=2
b=3
print(b+a)
print(b-a)
print(b*a)
print(a/b)
print(a**b)
print(a//b)
print(a%b)