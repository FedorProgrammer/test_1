N = int(input())  # Шишки
M = int(input())  # Орешки
K = int(input())  # Орешков необходимо

def supplies():
    if N * M >= K:
        return 'Белочки хватит!'
    else:
        return 'Не хватит!'

print(supplies())