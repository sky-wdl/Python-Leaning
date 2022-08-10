"""
实例2: Python蟒蛇绘制
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。
使用turtle库，绘制一个蟒蛇形状的图形。
注意：这不是自动评阅题目，仅用于练习，没有评阅。

"""
import turtle as t

t.setup(650, 350, 200, 200)  # 设置窗口属性（宽度像素值， 高度像素值， 以屏幕左上角为初始点x方向位置， 以屏幕左上角为初始点y方式位置）
t.penup()  # 抬起画笔
t.fd(-250)  # 以向右为初始方向，向后（屏幕左方向）移动250像素值。
t.pendown()  # 放下画笔
t.pensize(25)  # 设置画笔宽度为25个像素值
t.color("red")  # 画笔颜色为“红色”
t.seth(-40)  # 更改画笔的方向为负40度。（默认方向水平向右，即改为向左下角40度）
for i in range(4):
    # t.color("red")
    t.circle(40, 80)  # 控制画笔以曲线方式移动以40像素为半径，绘制80度弧度曲线。（以圆心在画笔正左侧90度方向，距离为40像素值的点距离绘制）
    # t.fd(40)
    # t.color("purple")
    t.circle(-40, 80)
    # t.fd(40)
# t.pencolor("red")
t.circle(40, 80/2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2/3)
t.done()