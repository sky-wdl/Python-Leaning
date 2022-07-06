zhStr = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '零']
numStr = input()
for out in numStr:
    print(zhStr[eval(out)-1], end='')