a = int(input())
b = int(input())
c = int(input())

value = a, b, c


if min(value) == a and max(value) == b:
    print(b - a)
elif min(value) == a and max(value) == c:
    print(c - a)
elif min(value) == b and max(value) == a:
    print(a - b)
elif min(value) == b and max(value) == c:
    print(c - b)
elif min(value) == c and max(value) == a:
    print(a - c)
elif min(value) == c and max(value) == b:
    print(b - c)