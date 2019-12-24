#!/usr/bin/env python
# -*- coding :utf-8 -*-
#author:shirenxiang time:2019/12/24 17:53
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != j) and (i !=k) and (j !=k):
                print (i,j,k)