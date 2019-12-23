"""
a = 10
b = 20

values = [x ** 2 for x in range(a, b + 1)]
print(values)

numbers = [x for x in values if x % 2 == 0]
print(numbers)

values = [100 if x < 200 else 400 for x in values]
print(values)
"""

a = 10
b = 20
values = [x for x in range(a, b + 1)]
print(values)

print('--')

b = 20
values = [2 ** x for x in range(0, b + 1)]
print(values)

print('--')

string = ['fjasdhufGbdshgvbuo', "edfbsdhbfi", "DGHSIOGUFGHI"]
upper_string = [x for x in string if x == x.upper()]
print(upper_string)

