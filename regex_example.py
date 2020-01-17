import re

pattern = re.compile('^[+][7]\d\d\d\d\d\d[-]\d\d[-]\d\d$')  # телефон
print(re.search(pattern, '+7999888-77-66'))

pattern = re.compile('\+7-?\d{3}-?\d{2}-?\d{2}')
print(re.search(pattern, '+79998887766'))

pattern = re.compile(('^[02468]$'))  # четные числа
print(re.search(pattern, '8'))

pattern = re.compile('(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[012])\.\d{4}')  # день.месяц.год
print(re.search(pattern, '02.11.2005'))