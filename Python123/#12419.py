"""
turtle风轮绘制
使用turtle库，绘制一个风轮效果，其中，每个风轮内角为45度，风轮边长150像素。
注意：这不是自动评阅题目，仅用于练习，没有评阅。
提示：turtle.goto(x,y)函数，能够将turtle画笔移动到坐标(x,y)
"""
import turtle as t

t.setup(700, 700, 200, 200)
t.pensize(5)
t.pencolor("black")
for i in range(4):
    t.right(90 * i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0, 0)

t.done()
