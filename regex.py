import re

pattern = re.compile('^world')  # создаем шаблон
value = 'world, hello'
print(re.search(pattern, value))  # поиск

pattern = re.compile('^\w\w\w$')
print(re.search(pattern, 'abF'))
print(re.search(pattern, "afsiyfguisdf"))

pattern = re.compile('\d\d\d')
print(re.search(pattern, 'Hello 4134'))

pattern = re.compile('^Hello,\s\w\w\w\w!')
print(re.search(pattern, 'Hello, Fedo!'))

pattern = re.compile("^\d{4}$")
print(re.search(pattern, '1234'))

pattern = re.compile('^\d{4,10}$')
print(re.search(pattern, '12345'))

pattern = re.compile('^\d{4,}$')
print(re.search(pattern, '1234254331345346436'))

pattern = re.compile('^\d{\d,\d}$')
print(re.search(pattern, '1{3,2}'))

pattern = re.compile('^\d\{3,4}$')
print(re.search(pattern, '1{3,4}'))

pattern = re.compile('^[abc]+$')
print(re.search(pattern, 'abcabcbacbcabacbbacb'))

pattern = re.compile('^[0-5]+$')
pattern = re.compile('^[b-z]+$')

pattern = re.compile('^(hello|world|something)$')