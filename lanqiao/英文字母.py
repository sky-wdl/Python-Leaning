"""
问题描述
输入一个正整数
�
n, 输出第
�
n 个大写英文字母。

输入格式
输入一行包含一个正整数
�
n 。

输出格式
输出一行包含一个字母。

样例输入 1

12
copy
样例输出 1

L
copy
样例输入 2

17
copy
样例输出 2

Q
"""

stR = list(range(65, 65+26))
n = int(input())
print(chr(stR[n-1]))
