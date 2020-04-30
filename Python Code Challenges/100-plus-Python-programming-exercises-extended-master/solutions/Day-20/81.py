a=[12,24,35,70,88,120,155]
b=[i for i in a if i%5==0 and i%7==0]
a=[i  for i in a if i not in b]





print(a)
