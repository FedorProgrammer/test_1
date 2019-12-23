number =123
# подсчитать сумму цифр числа
print(sum([int(x) for x in str(number)]))
number = 123
summa = 0
while number != 0:
    summa += number % 10
    number //= 10
print(summa)
print('--')
# подсчитать количество делителей
number = 123
count = 0
for i in range(2, number):
    if number % i == 0:
        count += 1
        print(i)
print(count)

print('--')

print(sum([1 if number % x == 0 else 0 for x in range(2, number)]))

print('--')

data = [123, 232, 2323]
for number in data:
    summa = 0
    while number != 0:
        summa += number % 10
        number //= 10
    print(summa)

print(data)

