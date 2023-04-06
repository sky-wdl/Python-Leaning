"""
题目描述
小蓝给学生们组织了一场考试，卷面总分为 100 分，每个学生的得分都是一个 0 到 100 的整数。

请计算这次考试的最高分、最低分和平均分。

输入描述
输入的第一行包含一个整数
�

(
1
≤
�
≤
1
0
4
)
n (1≤n≤10
4
 )，表示考试人数。

接下来
�
n 行，每行包含一个 0 至 100 的整数，表示一个学生的得分。

输出描述
输出三行。

第一行包含一个整数，表示最高分。

第二行包含一个整数，表示最低分。

第三行包含一个实数，四舍五入保留正好两位小数，表示平均分。

输入输出样例
示例
输入

7
80
92
56
74
88
99
10
copy
输出

99
10
71.29
"""

maX = 0
minI = 1000
suM = 0
numberPeople = int(input())
for i in range(numberPeople):
    temp = int(input())
    maX = max(maX, temp)
    minI = min(minI, temp)
    suM += temp
print(maX)
print(minI)
print("{:.2f}".format(suM/numberPeople))



