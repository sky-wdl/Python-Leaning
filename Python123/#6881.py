"""
实例4：文本进度条
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。
采用字符串方式打印可以动态变化的文本进度条，进度条需要能在一行中逐渐变化
要求如下：
(1) 采用sleep()模拟一个持续的进度,获得文本进度条的变化时间；
(2) 通过print()函数实现单行动态刷新，在print()函数中更换参数end的默认值为'',每次使用print()函数输出时不能换行；
(3) 要能回退：打印后光标到之前的位置 \r。
请在Windows的命令行（cmd或PowerShell）或其他操作系统的命令行下执行Python程序，获得进度条效果。
"""

import time

print("执行开始".center(25, '-'))
start = time.perf_counter()
for i in range(51):
    a = '*' * i
    b = '.' * (51 - i)
    c = i / 51
    dur = time.perf_counter() - start
    print("\r{:^3.0%}[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)
print("\n" + "执行结束".center(25, '-'))
