import random
print(random.sample(list(i for i in range(1,1001,2) if i%5==0 and i%7==0),5))
