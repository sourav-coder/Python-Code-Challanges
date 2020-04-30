a=[12,24,35,24,88,120,155,88,120,155]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:d[i]=1
b=[]
for i in d:print(i,end=' ')

