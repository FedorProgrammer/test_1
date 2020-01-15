import time


def run_timed(fun, *args): # *args передает аргументы
    begin_time = time.time()
    fun(*args)
    end_time = time.time()
    print(end_time - begin_time)

def second():
    summa = 0
    n = 1000
    for i in range(1, n):
        summa += i
    for i in range(1, n):
        summa += i


def third():
    pairs = []
    n = 100000
    for i in range(n):
        for j in range(n):
            pass

def bubble_sort(data):
    n = len(data)
    for i in range(n): # длинна текущего куска n - i
        for j in range(0, n - i - 1): # [0, n], [0, n - 1], [0, n - 2]
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    #data



def python_sort(data):
    sorted(data)

import random

numbers = []
numbers_for_python = []
n = 10000
for i in range(n):
    current_number = random.randint(0, 1000000000)
    numbers.append(current_number)
    numbers_for_python.append(current_number)

run_timed(bubble_sort, numbers)
run_timed(python_sort, numbers_for_python)
