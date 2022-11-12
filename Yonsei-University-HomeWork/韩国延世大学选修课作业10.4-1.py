"""
题目译文大意：
.编写程序,使可以将输入的两个单词的前后关系输出为不等号.
- 输入的单词为正常输入
- 输入的两个单词时是空格隔开的

示例input：
abc Abc
示例print
Abc > abc

示例input:
abc Bbc
示例print
abc > Bbc

示例input:
Yonsei Yonsei
示例print
Yonsei = Yousei
"""


def ascII(a):
    summation = 0
    for i in a:
        summation += ord(i)
    return summation


words_one, words_two = input("Enter two words>").split()

words_one_ascii = ascII(words_one)
words_two_ascii = ascII(words_two)

if words_one_ascii < words_two_ascii:
    print("{0:} > {1:}".format(words_two, words_one))
elif words_one_ascii > words_two_ascii:
    print("{0:} > {1:}".format(words_one, words_two))
elif words_one_ascii == words_two_ascii:
    print("{0:} = {1:}".format(words_one, words_two))
