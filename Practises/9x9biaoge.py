#!/usr/bin/env python
# -*- coding :utf-8 -*-
#author:shirenxiang time:2019/12/24 17:50
for i in range(1,10):
    for j in range (1,i+1):
        print('{}x{}={}\t'.format(j,i,i*j),end="")
    print()