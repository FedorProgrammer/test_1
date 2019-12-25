from typing import List

def sum_of_two_elements(a, b):
    '''
    функция для вычисления суммы двуч чисел
    :param a: первое число для суммы
    :type a: int
    :param b: второе число для суммы
    :type b: int
    :return: сумма двух чисел
    :rtype: int
    '''

    return a + b
print(sum_of_two_elements(1, 2))

print('--')

def find_positive_elements(data):
    """
    :type data: List[int]
    """
    result = []
    for element in data:
        if element > 0:
            result.append(element)
    return result

print(find_positive_elements([1, -2, 3, -5]))

print('--')

def my_join(*args, delimiter=' '):
    return delimiter.join(args)

print(my_join('Hello', 'world'))
print(my_join('a', 'b', 'c', 'd', delimiter=', '))
print('hello', 'world', '!', sep=', ', end='!!!')


def most_common_function(*args, **kwargs):
    print(args)
    print(kwargs)

most_common_function('hello', 'world', '!', sep=', ', end='!!!')

