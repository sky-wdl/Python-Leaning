"""
题目译文大致意思：

统计list的词频，转为dict,输出词频大于2的键值对
"""

words = ['The', 'LORD', 'is', 'my', 'shepherd', 'I', 'shall', 'not', 'be', 'in', 'want', 'He', 'makes', 'me', 'lie', 'down', 'in', 'green', 'pastures', 'he', 'leads', 'me', 'beside', 'quiet', 'waters', 'he', 'restores', 'my', 'soul', 'He', 'guides', 'me', 'in', 'paths', 'of', 'righteousness', 'for', 'his', 'names', 'sake', 'Even', 'though', 'I', 'walk', 'through', 'the', 'valley', 'of', 'the', 'shadow', 'of', 'death', 'I', 'will', 'fear', 'no', 'evil', 'for', 'you', 'are', 'with', 'me', 'your', 'rod', 'and', 'your', 'staff', 'they', 'comfort', 'me', 'You', 'prepare', 'a', 'table', 'before', 'me', 'in', 'the', 'presence', 'of', 'my', 'enemies', 'You', 'anoint', 'my', 'head', 'with', 'oil', 'my', 'cup', 'overflows', 'Surely', 'goodness', 'and', 'love', 'will', 'follow', 'me', 'all', 'the', 'days', 'of', 'my', 'life', 'and', 'I', 'will', 'dwell', 'in', 'the', 'house', 'of', 'the', 'LORD', 'forever']

a = {}
for i in words:
    if a. __contains__(i):
        a[i] = a[i] + 1
    else:
        a[i] = 1

for Key, value in a.items():
    if a[Key] > 2:
        print(Key, value)
    else:
        pass