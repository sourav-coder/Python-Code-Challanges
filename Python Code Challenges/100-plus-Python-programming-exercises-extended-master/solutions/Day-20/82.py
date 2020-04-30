a=[12,24,35,70,88,120,155]
b=[a[i] for i in range(0,len(a),2)]
for i in b:a.remove(i)




print(a)