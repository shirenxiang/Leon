#!/usr/bin/env python
# -*- coding :utf-8 -*-
#author:shirenxiang time:2019/12/24 17:56
# 引入日历
import calendar

# 输入指定年月
yy=int(input("数日年份："))
mm=int(input("输入月份:"))

#可以设置日历第一天为周日
calendar.setfirstweekday(firstweekday=6)
#显示日历
print(calendar.month(yy, mm))