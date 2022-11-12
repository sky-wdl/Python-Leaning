"""
用户登录的三次机会
给用户三次输入用户名和密码的机会，要求如下：
1）如输入第一行输入用户名为‘Kate’,第二行输入密码为‘666666’，输出‘登录成功！’，退出程序；
2）当一共有3次输入用户名或密码不正确输出“3次用户名或者密码均有误！退出程序。”。
输入示例1
Kate
666666

输出示例1
登录成功！
输入示例2
kate
123

alice
456

john
111111

输出示例2
3
次用户名或者密码均有误！退出程序。
平均代码量 10 行
"""

import sys

for count in range(3):
    account = input()
    password = input()
    if not (account == 'Kate' and password == '666666'):
        pass
    else:
        print("登录成功！")
        sys.exit()
print("3次用户名或者密码均有误！退出程序。")