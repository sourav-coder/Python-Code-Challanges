n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

c=set(a)^set(b)


print(c)