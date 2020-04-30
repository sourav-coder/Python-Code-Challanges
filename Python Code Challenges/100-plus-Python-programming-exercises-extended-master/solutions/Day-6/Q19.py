no=int(input())
from operator import itemgetter
a=[]
while no>0:
    no-=1
    n,age,s=map(str,input().split(','))
    age,s=int(age),int(s)
    a.append((n,age,s))
print(a)

a.sort(key=itemgetter(0,1,2))
print(a)

