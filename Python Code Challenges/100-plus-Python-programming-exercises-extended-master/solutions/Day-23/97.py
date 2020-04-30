
n=int(input())
p=1
a=[]
l=96+n
for i in range(1,n+(n-1)+2,2):

    print('  '*(n-p),end='')

    p+=1
    s=''
    for j in range(l,l-(i//2)-1,-1):
        print(chr(j),end=' ')
        s+=chr(j)
    st=''
    for k in range(len(s)-2,-1,-1):
        print(s[k],end=' ')
        st+=s[k]
    a.append(s+st)
    print()

p=1
for i in range(len(a)-2,-1,-1):
    print(' '*(p),end=' ')
    p+=1
    for j in a[i]:
        print(j,end=' ')
    if i==1:p+=1
    print()