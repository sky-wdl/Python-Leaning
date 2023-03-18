"""
获得用户输入的一个正整数输入，输出该数字对应的中文字符表示。
0到9对应的中文字符分别是：零一二三四五六七八九

    输入示例1
    123
    输出示例1
    一二三

    输入示例2
    9876543210
    输出示例2
    九八七六五四三二一零

平均代码量:4 行
"""
zhStr = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '零']
numStr = input()
for out in numStr:
    print(zhStr[eval(out) - 1], end='')