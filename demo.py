# 导入random模块
import random
from importlib import reload

random.seed(10)


def throw_yut1():
    a = random.random()
    if a <= 0.4:
        return '등'
    else:
        return '배'


# throw_yut4() 정의
#   반복문 안에서 throw_yut1()을 호출
#   在重复句中调用throw_yut1（）
#   4번 반복되며 result에 문자열이 누적되도록 함
#   重复4次并在result中累积字符串

def throw_yut4():
    result = ''

    for i in range(4):
        result += ''  # Edit ( 힌트: throw_yut1() 사용 )

    return result


for key in ['도', '개', '걸', '윷', '모']:
    print(f'{key} - {counts[key]} ({counts[key] / 1000 * 100:.1f}%)')
