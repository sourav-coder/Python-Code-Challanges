s=input()
a=[]
for i in set(s):
    a.append((i,s.count(i)))


a.sort(key=lambda x:x[1],reverse=True)
for i in a:
    print(i[0]+','+str(i[1]))
