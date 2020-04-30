
def recursion(n):

    if n==0 or n==1:
        return n
    else:

        return recursion(n-1)+recursion(n-2)
        
a=[]
n=int(input())
for i in range(n):

    a.append(str(recursion(i)))
print(','.join(a))
