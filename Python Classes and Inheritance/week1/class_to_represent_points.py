class Point():
    def getX(self):
        return self.x

point1 = Point()
point2 = Point()


point1.x = 5
point2.x = 10
##print(point1.x)
##print(point2.x)

print(point1.getX())
print(point2.getX())
