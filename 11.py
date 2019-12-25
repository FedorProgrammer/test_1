# Дана дата в форме "12.04.2019" требуется перевести в запись "12 апреля 2019"
months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель'
}

str_value = months.get(2)
if str_value is None:
    print('Wrong number')
else:
    print(str_value)

print('--')

for value in months:
    print(value)

print('--')

for value in months:
    print(months[value])

print('--')

keya = [value for value in months]
keys = months.keys()
print(keys)

print('--')

months[14] = 'Еще один месяц'
print(months[14])

print('--')

del months[14]
print(months.get(14))

print('--')

dictionary = {}

phones = set()
phones.add('123456')
phones.add("123457")
print(phones)

for element in phones:
    print(element)

print('--')

another_phones = set()
another_phones.add('123455')
another_phones.add('123453')
united_set = phones.union(another_phones) # Объединение множеств
print(united_set)

print('--')

intersect_set = phones.intersection(another_phones)
print(intersect_set)

print('--')

element = '123456'
if element in united_set:
    print('Yes')
else:
    print('No')

print('--')

