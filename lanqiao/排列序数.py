"""
https://www.lanqiao.cn/problems/269/learning/?first_category_id=1&sort=pass_rate&second_category_id=3&difficulty=20
"""

from itertools import permutations

s = list(input())
s2 = sorted(s)

cnt = 0
for i in permutations(s2, len(s2)):
    if list(i) == s:
        print(cnt)
        break
    cnt += 1
