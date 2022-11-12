"""
turtle正方形绘制
使用turtle库，绘制一个正方形。
注意：这不是自动评阅题目，仅用于练习，没有评阅。
"""

import turtle as t

t.setup(650, 350, 200, 200)
t.color("black")
t.pensize(25)
for i in range(1, 5):
    t.seth(90 * i)
    t.fd(100)
t.done()
