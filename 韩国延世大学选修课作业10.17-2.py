import random

random.seed(10)
result = None
back = None
belly = None
counts = {}


def throw_yut1():
    a = random.random()
    if a <= 0.4:
        return '등'
    else:
        return '배'


def throw_yut4():
    result = ''

    for i in range(4):
        result += throw_yut1()

    return result


for i in range(1000):
    result = throw_yut4()
    back = result.count('등')
    belly = result.count('배')

    if back == 3 and belly == 1:
        counts['도'] = counts.get('도', 0) + 1
    elif back == 2 and belly == 2:
        counts['개'] = counts.get('개', 0) + 1
    elif back == 1 and belly == 3:
        counts['걸'] = counts.get('걸', 0) + 1
    elif back == 0 and belly == 4:
        counts['윷'] = counts.get('윷', 0) + 1
    elif back == 4 and belly == 0:
        counts['모'] = counts.get('모', 0) + 1

for key in ['도', '개', '걸', '윷', '모']:
    print(f'{key} - {counts[key]} ({counts[key] / 1000 * 100:.1f}%)')
