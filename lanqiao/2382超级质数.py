"""
如果一个质数
�
P 的每位数字都是质数, 而且每两个相邻的数字组成的两位 数是质数, 而且每三位相邻的数字组成的三位数是质数, 依次类推, 如果每相 邻的
�
k 位数字组成的
�
k 位数都是质数, 则
�
P 称为超级质数。

如果把超级质数
�
P 看成一个字符串, 则这个超级质数的每个子串都是质 数。

例如, 53 是一个超级质数。

请问, 最大的超级质数是多少?
"""

primeNumber = [2, 3, 5, 7]
primeArrayOne = primeNumber.copy()
primeArrayTwe = []


# 判断是否为素数
def judgePrime(a):
    for y in range(2, a):
        if a % y == 0:
            return False
    return True


# 判断是否有连续相同的数字出现
# 如果出现连续的数字，则连续的数字可以看作一个该素数的子串
# 该子串因为数字是连续的，所以比不是素数，故需要排除掉，以满足题目的要求
def DoubleNumber(a):
    s = list(str(a))
    if len(s) < 3:
        return True
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True


# 枚举素数的组合并进行判断是否符合提议，符合提议的存入到primeArrayOne这个列表中
#
while 1:
    for x in primeArrayOne:
        for z in primeNumber:
            if judgePrime(x * 10 + z) and DoubleNumber(x * 10 + z):
                primeArrayTwe.append(x * 10 + z)
    if len(primeArrayTwe) >= 1:
        primeArrayOne.clear()
        primeArrayOne = primeArrayTwe.copy()
        primeArrayTwe.clear()
    else:
        break

primeArrayOne.sort()
print(primeArrayOne[len(primeArrayOne) - 1])
