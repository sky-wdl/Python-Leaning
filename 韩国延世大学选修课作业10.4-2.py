"""
题目译文大意：
2.对给定的字符串进行预处理，按出现的次数顺序输出排列的Top 10单词列表。

-预处理
删除 (, .;) 这几个标点符号
统一转换为大写字母
-排列成单词出现次数
重新制作(次数 单词)的list
按次数排序为 list.sort( reverse=True)
-输出符合格式的f-String
编号: 2 格
单词: 6 格， 右对齐
次数: 2 格

ps23 = '''The LORD is my shepherd, I shall not be in want.
He makes me lie down in green pastures, he leads me beside quiet waters,
he restores my soul. He guides me in paths of righteousness for his name's sake.
Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me.
You prepare a table before me in the presence of my enemies. You anoint my head with oil; my cup overflows.
Surely goodness and love will follow me all the days of my life, and I will dwell in the house of the LORD forever.'''
"""

ps23 = '''The LORD is my shepherd, I shall not be in want.
He makes me lie down in green pastures, he leads me beside quiet waters,
he restores my soul. He guides me in paths of righteousness for his name's sake.
Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me.
You prepare a table before me in the presence of my enemies. You anoint my head with oil; my cup overflows.
Surely goodness and love will follow me all the days of my life, and I will dwell in the house of the LORD forever.'''
ps23 = ps23.replace(',', '')
ps23 = ps23.replace('.', '')
ps23 = ps23.replace(';', '')
ps23 = ps23.upper()
ps23_list = ps23.split()
counts = {}
for i in ps23_list:
    counts[i] = counts.get(i, 0) + 1

ps23_list_sort = sorted(counts.items(), key=lambda x: x[1], reverse=True)
i = 1
for Dict, Value in ps23_list_sort[0:10]:
    print("{0:>2}）{1:>6} appeared {2:>2} times".format(i, Dict, Value))
    i = i + 1
