
# random 모듈 가져옴
import random

# 난수 발생을 일정한 패턴으로 고정하기 위한 코드
random.seed(10)

# throw_yut1() 함수 정의
#
#   '배' 아니면 '등'으로 결과값 반환 *random.random()은 한 번만 사용*
#   '배'가 반환될 확률 60% 으로
#   '등'이 반환될 확률 40% 으로
#
#   힌트) 10% 확률로 실행되는 코드: random.random() <= 0.1
#   힌트) 80% 확률로 실행되는 코드: random.random() <= 0.8


def throw_yut1():
    a = random.random()
    if a <= 0.4:
        return '등'
    else:
        return '배'
        

# throw_yut4() 정의
#   반복문 안에서 throw_yut1()을 호출
#   4번 반복되며 result에 문자열이 누적되도록 함

def throw_yut4():

    result = ''
    
    for i in range(4):
        result += throw_yut1()  # Edit ( 힌트: throw_yut1() 사용 )

    return result