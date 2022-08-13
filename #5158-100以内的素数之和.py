"""
100以内素数之和
描述
求100以内所有素数之和并输出。
素数指从大于1，且仅能被1和自己整除的整数。
提示：可以逐一判断100以内每个数是否为素数，然后求和。
输入格式
 该题目没有输入
"""

x = 0
for Number in range(2, 101):
    count = 0
    for i in range(2, Number):
        if Number % i == 0:
            count += 1
    if count == 0:
        x += Number
print(x)