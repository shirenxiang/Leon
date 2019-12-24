#!/usr/bin/env python
# -*- coding :utf-8 -*-
#author:shirenxiang time:2019/12/24 17:58
import turtle
import time

# 同时设置pencolor=color1, fillcolor=color2
turtle.color("red", "yellow")

turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()
turtle.mainloop()