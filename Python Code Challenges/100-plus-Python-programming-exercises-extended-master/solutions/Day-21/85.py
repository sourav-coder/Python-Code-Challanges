a=[12,24,35,70,88,120,155]
b=[a[i] for i in range(len(a))if i==0 or i==4 or i==5]
for i in b:
    a.remove(i)


print(a)

