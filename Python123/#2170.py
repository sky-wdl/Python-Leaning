"""
turtle叠边形绘制
使用turtle库，绘制一个叠边形，其中，叠边形内角为100度。
注意：这不是自动评阅题目，仅用于练习，没有评阅。
"""
import turtle as t

t.setup(700, 700, 200, 200)
t.pensize(5)
t.pencolor("black")
for i in range(9):
    t.fd(200)
    t.left(80)
t.done()
