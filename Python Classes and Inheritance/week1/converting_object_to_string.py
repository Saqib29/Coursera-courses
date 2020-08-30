class Point:
    """ Point class for representing manipulating x,y coordinates. """
    def __init__(self, intX, intY):
        self.x = intX
        self.y = intY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        self.s = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        return self.s
    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

p = Point(6,7)
p1 = Point(8, 9)

print(p)
print(p1)
  
