"""
定义get_circle_area()  输入一个字符串的半径，显示圆的面积

使用 math 模块的 pi 值
输入参数r
圆的面积公式: pi * r * r
将 str 转换为 float 时， 如果发生例外， 则返回 None

示例输入：
100
输出
31415.926535897932

示例输入：
abc
输出
None

示例输入：
12.3
输出
475.2915525615999
"""
import math


def get_circle_area(r):
    try:
        r = float(r)
        return math.pi * r * r
    except (ValueError, ArithmeticError):
        return None


n = input("Enter the radius of the circle>")
print(f'{get_circle_area(n)}')
