class Point:
    """ Point class fro representing and manipulating x,y coordinates. """

    def __init__(self, intX, intY):
        self.x = intX
        self.y = intY

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

    def __add__(self, otherpoint):
        return Point(self.x + otherpoint.x, self.y + otherpoint.y)

    def __sub__(self, otherpoint):
        return Point(self.x - otherpoint.x, self.y - otherpoint.y)

p1 = Point(-5, 10)
p2 = Point(15, 20)
print(p1)
print(p2)
# __add__
print(p1 + p2)
p3 = Point(1,2)
print(p1, p2+p3)

# __sub__
print(p1 - p3)
