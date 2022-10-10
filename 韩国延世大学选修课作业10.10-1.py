"""
题目译文大意：
请编写输入体重和身高后能输出当前体重状态的程序。
定义/使用以下两个函数:
Bmi() - 输入体重和身高后输出身体的BMI指数
weight_status() - 输入BMI指数后返回到weight statu

"""


def bmi(weight, height):
    weight_status((weight / height ** 2) * (0.1 ** 4))


def weight_status(Bmi):
    if Bmi > 30.0:
        print("Weight status: [Obses]")
    elif 25.0 < Bmi <= 30.0:
        print("Weight status: [Overweight]")
    elif 18.0 <= Bmi <= 25.0:
        print("Weight status: [Normal]")
    elif Bmi <= 18.5:
        print("Weight status: [Underweight]")


w = input("Weight(kg)>")
h = input("Height(cm)>")
bmi(eval(w), eval(h))
