n = 4
m = 5
matrix = [[0 for y in range(m)] for x in range(n)]
print(matrix)

print('--')

for row in matrix:
    for elements in row:
        print(elements, end=' ')
    print()
print('--')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

print('--')

N = 10

data = [[0 for y in range(n)] for x in range(n)]

for row in range(len(data)):
    for column in range(len(data[row])):
        data[row][column] = (row + 1) * (column + 1)
        print(data[row][column], end=' ')
    print()

print('--')

first = [1, 2, 3]
second = [4, 5, 6]
result = [x + y for x in first for y in second]
print(result)

print('--')

a = 12
b =23
maximum = b if b > a else a  # тернарный оператор сравнения
