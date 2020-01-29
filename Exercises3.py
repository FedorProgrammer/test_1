C = int(input())
H = int(input())
O = int(input())

def Alc():
    c = 0
    h = 0
    if C >= 2 and C % 2 == 0:
         c = C // 2

    if H >= 6 and H % 6 == 0:
        h = H // 6
        c = min(c, h)

    if O >= 1 and O % 1 == 0:
        o = O // 1
        c = min(c, h, o)
    return c


print(Alc())
