a=list(map(int,input().split(',')))
# print(a)
b=[a[i]*a[i] for i in range(0,len(a),2)]
for i in b:print(i,end=',')
