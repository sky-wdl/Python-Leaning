"""
turtle六边形绘制
使用turtle库，绘制一个六边形。
注意：这不是自动评阅题目，仅用于练习，没有评阅。
"""

import turtle as t

t.setup(650, 650, 200, 200)
t.pencolor("black")
t.pensize(10)
for i in range(1, 7):
    t.fd(100)
    # t.seth(60 * i)
    t.left(60)
t.done()
