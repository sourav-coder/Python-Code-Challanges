s=input()
c=0

d=0
for i in s:
    if i.isupper():c+=1
    elif i.islower():d+=1
print('Upper:%d'%c)
print('Lower:%d'%d)
