"""
问题描述
给定
�
n 个整数
�
1
,
�
2
,
⋅
⋅
⋅
,
�
�
a
1
​
 ,a
2
​
 ,⋅⋅⋅,a
n
​
  ，求它们两两相乘再相加的和，即：

�
=
�
1
⋅
�
2
+
�
1
⋅
�
3
+
⋯
+
�
1
⋅
�
�
+
�
2
⋅
�
3
+
⋯
+
�
�
−
2
⋅
�
�
−
1
+
�
�
−
2
⋅
�
�
+
�
�
−
1
⋅
�
�
S=a
1
​
 ⋅a
2
​
 +a
1
​
 ⋅a
3
​
 +⋯+a
1
​
 ⋅a
n
​
 +a
2
​
 ⋅a
3
​
 +⋯+a
n−2
​
 ⋅a
n−1
​
 +a
n−2
​
 ⋅a
n
​
 +a
n−1
​
 ⋅a
n
​

输入格式
输入的第一行包含一个整数
�
n。

第二行包含
�
n 个整数
�
1
,
�
2
,
⋯
,
�
�
a
1
​
 ,a
2
​
 ,⋯,a
n
​
 。

输出格式
输出一个整数
�
S，表示所求的和。请使用合适的数据类型进行运算。

样例输入
4
1 3 6 9
copy
样例输出
117
"""

userNumber = int(input())
numbers = input().split(' ')
suM = list(range(userNumber))
suM[0] = 0
numbersSum = 0

for i in range(userNumber):
    if i == 0:
        suM[i] = int(numbers[i])
    else:
        suM[i] = suM[i - 1] + int(numbers[i])

for i in range(userNumber):
    numbersSum += int(numbers[i]) * (suM[userNumber - 1] - suM[i])

print(numbersSum)
