class KNumber(object):
    num_name = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']

    def __init__(self, num):
        self.number = num

    def __str__(self):
        if self.number >= 0:
            return f'{self.num_name[self.number]}'
        else:
            self.number *= -1
            return f'마이너스 {self.num_name[self.number]}'


for i in range(-10, 11):
    print(f'{i:3}: {KNumber(i)}')
