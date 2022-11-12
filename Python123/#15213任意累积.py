"""
任意累积
请根据编程模板补充代码，计算任意个输入数字的乘积。
注意，仅需要在标注...的地方补充一行或多行代码。
输入示例1
1,2,3,4

输出示例1
24
------------此题未完成------------
"""


def cmul(n):
    c = 1
    for i in range(len(n) + 1):
        c = c + n[i - 1] * [i]
        print(c)
        return c

print(eval("cmul({})".format(input())))
