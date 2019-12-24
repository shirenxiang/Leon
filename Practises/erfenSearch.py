#!/usr/bin/env python
# -*- coding :utf-8 -*-
#author:shirenxiang time:2019/12/24 17:54
'''递归查找'''
"""有一个list集合arr=【1,3,4,6,7,8,10,13,14】要在其中查找自己想要的数"""
#返回x在arr中的索引位置，如果没有的话则返回-1
def binarySearch (arr, l, r, x):
    #基本判断
    if r>=l:
        mid=int(l+(r-1)/2)

        #元素正好在中间位置
        if(arr[mid]==x):
            return mid
        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid]>x:
            return binarySearch(arr,1,mid-1,x)
        # 元素大于中间位置的元素，只需要再比较右边的元素
        elif arr[mid]<x:
            return binarySearch(arr,mid+1,r,x)
        else:
            # 不存在
            return -1

# 测试数组
arr=[2,3,4,10,40]
x=10

#函数调用
result=binarySearch(arr,0,len(arr)-1,x)

if result != -1:
    print("元素在数组中的索引为 %d:" %result)
    print(arr[3])
else:
    print("元素不在数组中")