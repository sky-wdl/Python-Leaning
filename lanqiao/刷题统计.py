"""
问题描述
小明决定从下周一开始努力刷题准备蓝桥杯竞赛。他计划周一至周五每天 做
�
a 道题目, 周六和周日每天做
�
b 道题目。请你帮小明计算, 按照计划他将在 第几天实现做题数大于等于
�
n 题?

输入格式
输入一行包含三个整数
�
,
�
a,b 和
�
n.

输出格式
输出一个整数代表天数。

样例输入
10 20 99
copy
样例输出
8
"""

a, b, n = input().split()
a = int(a)
b = int(b)
n = int(n)
cnt = 0
cntTemp = 0

if n <= (a*5 + b*2):
    while n > 0:
        if cntTemp < 5:
            cntTemp += 1
            n -= a
            cnt += 1
        elif cntTemp == 7:
            cntTemp = 0
        else:
            cntTemp += 1
            n -= b
            cnt += 1
else:
    cnt = (n // (a*5 + b*2)) * 7
    n = n % (a*5 + b*2)
    while n > 0:
        if cntTemp < 5:
            cntTemp += 1
            n -= a
            cnt += 1
        elif cntTemp == 7:
            cntTemp = 0
        else:
            cntTemp += 1
            n -= b
            cnt += 1

print(cnt)

