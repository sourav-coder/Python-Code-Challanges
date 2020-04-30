x,y=map(int,input().split())
a=[]
for i in range(x):
    b=[]
    for  j in range(y):
        b.append(i*j)
    a.append(b)
print(a)
