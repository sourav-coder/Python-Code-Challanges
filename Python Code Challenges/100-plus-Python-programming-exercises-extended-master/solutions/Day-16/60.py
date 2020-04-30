def recursion(n,c):
    if n==0:
        return c
    else:
        c+=100
        return recursion(n-1,c)
        
n=int(input())
print(recursion(n,0))
