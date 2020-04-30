class American(object):
    def __init__(self,n):
        self.name=n
    def display(self):
        print(self.name)

class NewWorker(American):
    pass

x=NewWorker('Yasin')
x.display()


