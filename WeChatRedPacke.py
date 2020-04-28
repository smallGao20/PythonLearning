import  random

class RedMoney():


    def SetMoney(self):
        self.money = float(input("请输入金额"))
        self.num = int(input("请设置红包个数"))
        self.kind = int(input("请设置红包种类"))
        if self.money / self.num < 0.01:
            print("红包金额不足，无法建立拼手气红包")
            self.num = self.money / 0.01
            print("红包数量自动更改为 ",self.num)
        if self.kind == 1 and (self.money * 100) % self.num != 0:
            print("该金额无法均匀分配！")
            temp = 100 * self.money
            temp = self.money * 100 - temp % self.num
            self.money = temp / 100
            print("金额自动修正为 ",self.money)

    def GetMoney(self):
        i = 1
        self.money = self.money * 100
        # 给予实际情况，该种状况下所有情况下金额均为整数
        if self.kind == 1:
            while (self.num > 0 and self.money > 0):
                temp = (self.money / self.num) / 100
                print("No.", i, " money:",temp)
                i += 1
                if (i == self.num + 1):
                    self.money = 0

        else:
            while (self.num > 0 and self.money > 0):
                # print("money ",self.money,"num ",self.num)
                if self.num > 1:
                    temp = self.money - self.num + 1
                    temp = random.randint(1,temp)
                    self.money = self.money  - temp
                    # print("we can using :", temp/100)
                    print("No.", i, " money:", temp/100)
                    self.num -= 1
                    i += 1
                else:
                    print("No.", i, " money:",self.money/100)
                    self.money = 0
                    self.num = 0




while (1):
    r = RedMoney()
    r.SetMoney()
    r.GetMoney()

# 该段程序用于模拟微红包的工作方式（普通红包和拼手气红包）
# 代码优点：
# 1. 该段代码采用随机数生成的方式，支持精度为0.01级别的运算，但只是模拟
# 2. 该段代码以保持金额减少或者金额不变的前提下能够自动修正金额或者数量以满足程序的正产运行
# 3. 采用类的方式完成模拟操作能够较为贴合实际的辅助完成工作
# 代码缺点：
# 1. 类的公有私有成员不做区分，安全性低
# 2. 全程基于整数类类型的运算，运算范围限制较大
# 3. 程序代码结构中由于基于逻辑清晰的问题导致代码冗余量大