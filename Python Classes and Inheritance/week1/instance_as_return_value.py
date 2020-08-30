class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    def getX():
        return self.x
    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y **2 )) ** 0.5

    def halfway(self, target):
        mx = (self.x + target.x) // 2
        mn = (self.y + target.y) // 2
        return Point(mx, mn)

    def lele(self, target):
        return Point(self.x , target.y)

    def __str__(self):
        return 'x = {}, y = {}'.format(self.x, self.y)

p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)   # sent two instances 
print(mid)


le = p.lele(q) # I can define functin in my wish
print(le)
