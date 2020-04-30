def binary(a,n):
    l=0
    r=len(a)-1
    while l<=r:
        mid=(l+r)//2
        if a[mid]==n:return mid
        elif n>a[mid]:l=mid+1
        else:r=mid

a=[2,4,6,8,10]
print(binary(a,2))