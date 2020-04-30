def recursion(n):
    if n==0 or n==1:
        return n
    else:
        
        return recursion(n-1)+recursion(n-2)
        
n=int(input())
print(recursion(n))
