class Cat():

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def Meow(self):
        return "meow!!!!!!!!!!!!!!!!!"

a = Cat('Барсик', 'Black', 3)

print(a.Meow())

print('--')

class Animal():

    def __init__(self, name):
        self.name = name


    def eat(self):
        return "Приятного аппетита!"

    def getName(self):
        return self.name

    def setName(self):
        self.name = input('Введите новое имя: ')
        return self.name

    def makeNoise(self):
        return self.name + " говорит: 'гррррр' "

a = Animal('Барсик')

print(a.makeNoise())

print(a.getName())

print(a.eat())

print(a.setName())
