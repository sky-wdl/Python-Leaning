"""
Hello World的条件输出
描述
获得用户输入的一个整数，参考该整数值，打印输出"Hello World"，要求：
如果输入值是0，直接输出"Hello World"
如果输入值大于0，以两个字符一行方式输出"Hello World"（空格也是字符）
如果输入值小于0，以垂直方式输出"Hello World"
"""
Str = input()
if Str == '0':
    print("Hello World")
elif eval(Str) > 0:
    print("He\nll\no \nWo\nrl\nd")
elif eval(Str) < 0:
    for Str in ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']:
        print(Str)