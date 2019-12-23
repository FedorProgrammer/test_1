values = []
k = 10
n = 4
for k in range(1, n + 1):
    for i in range(k):
        values.append(k)
print(values)

print('--')

values = [k for k in range(1, n + 1) for i in range(k)]
print(values)

print('--')

# Сапер
n = 5
m = 5
bomb = 9
matrix = [[0 for i in range(n)] for j in range(m)]
matrix[0][1] = bomb
matrix[2][3] = bomb
matrix[2][1] = bomb
print(matrix)
x = 1
y = 1
matrix.insert(0, [0] * (n + 2)) # строчка в начале
matrix.append([0] * (n + 2)) # строчка в конце
for i in range(1, m + 1): # строчка между
    matrix[i].append(0)
    matrix[i].insert(0, 0)
print(matrix)
# смещаем точку в новом поле
x += 1
y += 1
bomb_count = 0
for i in range(-1, 2):
    for j in range(-1, 2):
        if matrix[x + i][i + j] == bomb:
            bomb_count += 1
print(bomb_count)

for row in range(m):
    for column in range(n):
        x = row + 1
        y = column + 1
        if matrix[x][y] != bomb:
            bomb_count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if matrix[x + i][i + j] == bomb:
                        bomb_count += 1
            matrix[x][y] = bomb_count

for row in matrix:
    print(row)

print('--')
# Змейка
result = []
n = 4
for i in range(n):
    current_list = [x for x in range(n * i + 1, n * (i + 1) + 1)]
    if i % 2 == 1:
        current_list.reverse()
    result.append(current_list)
for row in result:
    print(row)

print('--')

x = 0
y = 0
direction = 0
n = 3
result = [[0 for i in range(n)] for j in range(n)] # создаем матрицу
current = 1
#for value in range (1, n * n + 1):
print(x, y, current)
while current < n * n + 1:
    if result[x][y] == 0:
        result[x][y] = current
        current += 1

    if direction == 0: # движение вправо
        if y + 1 < n:
            y += 1
        else:
            direction += 1 # идем вниз
    elif direction == 1: # движение вниз
        if x + 1 < n:
            x += 1
        else:
            direction += 1 # идем влево
    elif direction == 2:
        if y - 1 >= 0:
            y -= 1
        else:
            direction += 1
    elif direction == 3:
        if x - 1 >= 0:
            x -= 1
        else:
            direction = 0


for row in result:
    print(row)