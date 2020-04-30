s=input()
d={}
for i in s:
    if i in d:d[i]+=1
    else:d[i]=1

for key,val in d.items():
    print(key+','+str(val))

