class Fruit:
    def __init__(self, fruit, price):
        self.name = fruit
        self.price = price

    def sort_priority(self):
        return self.price

L = [
        Fruit('Cherry', 10),
        Fruit('Apple', 5),
        Fruit('Blueberry', 20)
    ]
##
##for fruit in sorted(L, key=Fruit.sort_priority, reverse=True):
##    print(fruit.name)


# we can use lambda function too
for fruit in sorted(L, key=lambda x: x.sort_priority(), reverse=True):
    print(fruit.name)
