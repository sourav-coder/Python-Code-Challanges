import timeit
s=timeit.default_timer()
i=2
for _ in range(100):
    i+=2

e=timeit.default_timer()
print(e-s)


