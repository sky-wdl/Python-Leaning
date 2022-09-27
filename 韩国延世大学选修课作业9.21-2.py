"""
中文译文如下：

请填写每日福利利息计算程序。
输入初始金额、利率后,1~30天的余额以重复文表示。
小数点以下值即使不一致也OK假设用户输入正常金额和利率,两者均转换为float如果金额达到最初金额的2倍以上,则输出以下信息并反复退出Your investment is doubled! 利率以%为单位,在公式中计算前应分配100。
"""

investment = float(eval(input("initial investment>")))
interest = input("daily initial Rate(%)>")

interest = interest[:-1]
interest = float(eval(interest))
value = investment

for i in range(1, 31):
    investment = investment * (interest * 0.01 + 1.0)
    if investment <= 2 * value:
        print(i, investment)
    else:
        print("Your investment is double!")
        break