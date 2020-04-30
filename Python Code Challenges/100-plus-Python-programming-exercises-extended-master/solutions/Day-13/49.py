class Shape(object):
 

    def area(self,s=0):
        print(s*s)


    


class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        super().area(self.side)

d=Square(4)
d.area()