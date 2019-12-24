#!/usr/bin/env python
# -*- coding :utf-8 -*-
#author:shirenxiang time:2019/12/24 17:53
def bubblesort(arr):
    n=len(arr)
    # 遍历数组所有元素
    for i in range(n):

        #Lastet i elements are already in place
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[64, 34, 25, 12, 22, 11, 90]

# 调用方法
bubblesort(arr)

# 打印
print("排序后的数组为:")
for i in range(len(arr)):
    print("%d"%arr[i])