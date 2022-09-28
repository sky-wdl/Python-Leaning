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
        pass
    else:
        a[i] = 1
b = []
i = 0
for Key, value in a.items():
    if i == 10:
        break
    else:
        for s in range(value):
            b.append(Key)
        i += 1
print(b)


# a = set()
# for i in words:
#     a.add(i)
# a = list(a)
# b =[]
# for i in range(10):
#     b.append(a[i])
# print(b)