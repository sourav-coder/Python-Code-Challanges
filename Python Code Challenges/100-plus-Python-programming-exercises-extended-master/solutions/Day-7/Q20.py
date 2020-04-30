class generate(object):
    def __init__(self):
        self.a=[]
    def gen(self,n):
        if n&2==1:n+=1
        for i in range(0,n,2):
            if i%7==0:
                yield i


x=generate()
for i in x.gen(int(input())):
    print(i,end=',')

# print(list(x.gen(50)))
    
