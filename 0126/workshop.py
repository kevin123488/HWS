class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, p1, p2):
        # self.x1 = p1.x
        # self.y1 = p1.y
        # self.x2 = p2.x
        # self.y2 = p2.y
        self.p1 = p1
        self.p2 = p2
        self.width = abs(p1.x - p2.x)
        self.height = abs(p1.y - p2.y)

    def get_area(self):
        # 함수니까 함수 쓰는 방식 따라가자..
        # width = abs(self.p1.x - self.p2.x)
        # height = abs(self.p1.y - self.p2.y)
        # return width * height
        # return abs((self.p1.x - self.p2.x) * (self.p1.y - self.p2.y))
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2
    
    def is_square(self):
        # width = abs(self.p1.x - self.p2.x)
        # height = abs(self.p1.y - self.p2.y)
        # if width == height:
        #     return True
        # else:
        #     return False
        return self.width == self.height

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())