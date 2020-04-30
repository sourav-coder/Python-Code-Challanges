class Rectangle(object):
    def __init__(self,l,b):
        self.length,self.breadth=l,b
    
    def area(self):
        
        print(self.length*self.breadth)

x=Rectangle(2,3)
x.area()
