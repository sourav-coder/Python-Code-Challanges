n=int(input())
a=[]
for _ in range(n):a.append(input())


from collections import  OrderedDict
d=OrderedDict()
for i in a:
    if i in d:d[i]+=1
    else:d[i]=1
print(len(d))
for i in d.values():
    print(i,end=' ')
