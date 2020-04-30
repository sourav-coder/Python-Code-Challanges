def gen(n):
    for i in range(0,n+1,2):
        yield str(i)



a=list(gen(int(input())))

print(','.join(a))
