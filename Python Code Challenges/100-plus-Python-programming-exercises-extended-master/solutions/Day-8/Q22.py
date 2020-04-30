s=input().split(' ')
from collections import Counter
z=Counter(s).most_common()
print(z)
z.sort(key=lambda x:x[0])
print(dict(z))
