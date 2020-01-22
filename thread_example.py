import threading


def foo1():
    for i in range(100):
        print('1')

def foo2():
    for i in range(100):
        print('2')



thread1 = threading.Thread(target=foo1)  # создай поток который выполняет foo1
tread2 = threading.Thread(target=foo2)

thread1.start()  # стартуем
tread2.start()


