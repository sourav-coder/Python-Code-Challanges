n=int(input())
x,y=0,0
for _ in range(n):
    a,b=map(str,input().split())
    b=int(b)
    if a=='LEFT':x-=b
    elif a=='Right'.upper():x+=b
    elif a=='UP':y+=b
    else:y-=b
# print(x,y)
import math as m
print(int(m.sqrt(x**2+y**2)))

