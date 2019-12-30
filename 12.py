class BankClient():
    min_life = 15 * 12
    def __init__(self, name, age, inc, status):
        self.name = name
        self.age = age
        self.inc = inc
        self.status = status

    def get_month_inc(self):
        return self.inc / 12

    def accept_credit(self, value):
        pay_time = 70 - self.age
        if (self.inc - value / pay_time - self.min_life) > 0 and (pay_time > 0):
            return True
        else:
            return False
        


max = BankClient("Max", 15, 1000, "investor")

print(max.age)

print(max.get_month_inc())
print(max.accept_credit(100))