class string(object):
    def __init__(self):
        self.string=''
    def getstring(self):
        self.string=input()
    def printstring(self):
        print(self.string.upper())


x=string()
x.getstring()

x.printstring()

