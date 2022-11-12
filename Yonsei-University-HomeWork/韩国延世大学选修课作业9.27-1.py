"""
译文大致意思：
按照list的形式输出包含十个不重复的字符，该十个字符的排列顺序按照words list中的先后出现顺序进行排列。
"""


words = ['The', 'LORD', 'is', 'my', 'shepherd', 'I', 'shall', 'not', 'be', 'in', 'want', 'He', 'makes', 'me', 'lie',
         'down', 'in', 'green', 'pastures', 'he', 'leads', 'me', 'beside', 'quiet', 'waters', 'he', 'restores', 'my',
         'soul', 'He', 'guides', 'me', 'in', 'paths', 'of', 'righteousness', 'for', 'his', 'names', 'sake', 'Even',
         'though', 'I', 'walk', 'through', 'the', 'valley', 'of', 'the', 'shadow', 'of', 'death', 'I', 'will', 'fear',
         'no', 'evil', 'for', 'you', 'are', 'with', 'me', 'your', 'rod', 'and', 'your', 'staff', 'they', 'comfort',
         'me', 'You', 'prepare', 'a', 'table', 'before', 'me', 'in', 'the', 'presence', 'of', 'my', 'enemies', 'You',
         'anoint', 'my', 'head', 'with', 'oil', 'my', 'cup', 'overflows', 'Surely', 'goodness', 'and', 'love', 'will',
         'follow', 'me', 'all', 'the', 'days', 'of', 'my', 'life', 'and', 'I', 'will', 'dwell', 'in', 'the', 'house',
         'of', 'the', 'LORD', 'forever']
a = {}
for i in words:
    if a. __contains__(i):
        a[i] = a[i] + 1
    else:
        a[i] = 1
b = []
i = 0
for Key, value in a.items():
    if i == 10:
        break
    else:
        b.append(Key)
        i += 1
print(b)
