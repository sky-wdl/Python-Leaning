"""
定义一种银行用户 class User
magic method( 创建者) _ _ init _ _: 重置为名称和余额
send_to() : 汇款method
参数:收件人、金额
receive_from():汇款method
参数:发送人，金额
magic method _ _ str _:
输出余额和存取款记录

"""


class User(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)
        self.history = []

    def send_to(self, recipient, amount):
        # 接收者信息
        if int(amount) <= int(self.balance):
            self.balance -= amount
            self.history.append(f'send {amount} to {recipient.name}')
            self.receive_from(recipient, amount)
        else:
            print("Sorry, the balance is insufficient!\n")

    def receive_from(self, sender, amount):
        # 发送人信息
        sender.balance += amount
        sender.history.append(f'received {amount} from {self.name}')

    def __str__(self):
        result = f'{self.name} ({self.balance})\n'
        for item in self.history:
            result += '\t' + item + '\n'

        return result


# No edit

kim = User('김연세', 5000)
hong = User('홍길동', 2000)
eagle = User('독수리', 6000)

print(kim)
print(eagle)

print('---')

kim.send_to(hong, 500)
eagle.send_to(hong, 500)
hong.send_to(eagle, 100)
eagle.send_to(kim, 3000)

print(kim)
print(eagle)
