"""
题目译文大意：
[通过出生日期了解朝鲜时代时期的我的名字]
定义 get_chosun_name() 函数
参数: m, d
返回值:朝鲜时代名称
用户输入整数（非正常输入时输出"错误输入"）
假设所有月份截止到31日
"""


def get_chosun_name(month, day):
    name1 = ['쌍', '계', '창', '돌', '삼', '갑', '육', '방', '말', '경', '병', '맹']
    name2 = ['자', '실', '무', '숙', '분', '봉', '년', '놈', '석', '식', '걸', '룡', '순', '나', '창', '란', '렬', '실', '경', '종', '덕',
             '득', '복', '동', '꽁', '중', '신', '미', '오', '욕', '님']

    if (not (m>12 or m<1)) and (not (d>31 or d<1)) :
        return name1[month+1]+name2[day+1]
    else:
        return False


m = eval(input('태어난 월>'))
d = eval(input('태어난 일>'))

if get_chosun_name(m, d):
    print('당신의 조선시대 이름은: '+get_chosun_name(m, d))
else:
    print('잘못된 입력')