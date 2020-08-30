class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

point1 = Point(5, 10)
point2 = Point(1, 2)

print(point1.getX())
print(point2.getX())
