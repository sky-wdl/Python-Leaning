"""
实例5：身体质量指数BMI
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。
bmi ：Body Mass Index 国际上常用地衡量人体肥胖和健康程度重要标准，主要用于统计分析
定义：bmi = 体重 (kg) /身高2(m2)
获取用户输入的体重和身高值，计算并给出国际和国内的 bmi 分类

要求如下：
(1) 混合计算并给出国际和国内的 bmi 分类；
(2) 使用input()获得测试用例输入时，不要增加提示字符串。
"""


def CHN_BMI(bmi):
    if bmi >= 28:
        return "肥胖"
    elif 24 <= bmi < 28:
        return "偏胖"
    elif 18.5 <= bmi < 24:
        return "正常"
    elif bmi < 18.5:
        return "偏瘦"


def ISO_BMI(bmi):
    if bmi >= 30:
        return "肥胖"
    elif 25 <= bmi < 30:
        return "偏胖"
    elif 18.5 <= bmi < 25:
        return "正常"
    elif bmi < 18.5:
        return "偏瘦"


height, weight = eval(input())
BMI = weight / pow(height, 2)
print("BMI数值为:{:.2f}".format(BMI) + '\n' + "BMI指标为:国际'{0:}',国内'{1:}'".format(ISO_BMI(BMI), CHN_BMI(BMI), BMI))
