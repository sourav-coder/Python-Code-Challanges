def gen(n):
    for i in range(0,n+1):

        if i%5==0 and i%7==0:
            yield str(i)




a=list(gen(int(input())))

print(','.join(a))
