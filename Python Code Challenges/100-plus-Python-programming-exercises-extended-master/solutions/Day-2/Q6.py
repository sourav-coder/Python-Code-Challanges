import math as m
s=input()

s=s.split(',')
c,h=50,30
for i in s:
    print(int(m.sqrt((2*c*int(i))/h)),end=',')


