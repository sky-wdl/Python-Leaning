"""
turtle八边形绘制
 
描述
使用turtle库，绘制一个八边形。
注意：这是一个自动评阅题目，请补充"编程模板"中横线内容，横线不保留。
"""
import turtle as t
t.pensize(2)
for i in range(8):
    t.fd(100)
    t.left(45)