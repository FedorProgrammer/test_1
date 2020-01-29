def root(a):
    if a == 1 or a == 4 or a == 6 or a == 8 or a == 9:
        return 0
    for number in range(2, a):
        if a % number == 0:
            return sum(map(int, str(a)))
    return a

print(root(128))
print(root(3))
print(root(9))
print(root(5))