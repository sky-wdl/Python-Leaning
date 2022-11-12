"""
实例6：圆周率的计算
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。
求解圆周率可以采用蒙特卡罗方法，在一个正方形中撒点，根据在1/4圆内点的数量占总撒点数的比例计算圆周率值。
请以123作为随机数种子，获得用户输入的撒点数量，编写程序输出圆周率的值，保留小数点后6位。
输入示例
1024
输出示例
3.218750
"""

import random

random.seed(123)
frequency = eval(input())
count = 0.0
for coordinate in range(frequency):
    x, y = random.random(), random.random()
    if pow((pow(x, 2) + pow(y, 2)), 0.5) <= 1:
        count += 1
print("{:.6f}".format(4 * count / frequency))