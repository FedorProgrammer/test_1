class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return 'x=' + str(self.x) + ", y=" + str(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
p = Point(1, 2)
p1 = Point()
p1.x = 1
p1.y = 2

p2 = Point(2, 4)
p3 = p2 + p1
print(p3)
# x=3, y=6
print(p1 == p2)
# False
print(p1 == Point(1, 2))
# True
