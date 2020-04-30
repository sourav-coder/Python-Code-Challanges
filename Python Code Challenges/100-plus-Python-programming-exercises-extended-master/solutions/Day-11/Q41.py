def fun(a):
    for i in a:
        yield i**2


a=[1,2,3,4,5,6,7,8,9,10]
l=list(fun(a))

print(l)

