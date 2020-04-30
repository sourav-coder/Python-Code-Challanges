a=[]
for i in range(2002,3201):
    if i%7==0 and i%5!=0:a.append(str(i))
print(','.join(a))