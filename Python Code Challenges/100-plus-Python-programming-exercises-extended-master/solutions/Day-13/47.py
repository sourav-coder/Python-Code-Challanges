class Circle(object):
    def __init__(self,r):
        self.radius=r
    
    def area(self):
        import math as m
        
        print(m.pi*self.radius**2)

x=Circle(2)
x.area()
