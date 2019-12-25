def max_of_numbers(a, b, c):
    return max(a, b, c)
print(max_of_numbers(10, 9, 18))

def year(data):
    if data % 4 == 0 and data % 100 != 0:
        return 'Yes'
    else:
        return 'No'

print(year(1982))

def Hip(a, b):     # гипотенуза
    return (a ** 2 + b ** 2) ** 1/2
print(Hip(10, 10))

def simple_number(a):
    for i in range(2, a):
        if a % i == 0:
            return 'No'
    return 'Yes'

print(simple_number(7))
print(simple_number(243756438725))
