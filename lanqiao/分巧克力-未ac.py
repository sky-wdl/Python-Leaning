N, K = input().split(' ')
N = int(N)
K = int(K)

# 短边
chocolateWidth = list(range(N))
# 长边
chocolateLength = list(range(N))
# 每人手中分到的巧克力最大边长数
chocolateMax = 10 ** 5 + 1
# 每人手中分到的巧克力最短边长数
chocolateMini = 1


for i in range(N):
    tempLeft, tempRight = input().split(' ')
    chocolateWidth[i], chocolateLength[i] = int(tempLeft), int(tempRight)
    chocolateMax = min(chocolateMax, int(tempLeft), int(tempRight))

while True:
    # 分了多少块
    chocolateCnt = 0

    for i in range(N):
        chocolateCnt += ((chocolateLength[i] // chocolateMax) * (chocolateWidth[i] // chocolateMax))
    if chocolateCnt >= K:
        print(chocolateMax)
        break
    else:
        chocolateMax -= 1
