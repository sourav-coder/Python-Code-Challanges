e=input()
import string
s=''
for i in e:
    if i not  in string.punctuation:
        s+=i

import re
d=re.findall(r'\d',s)
print('Digits:%d'%len(d))
e=re.findall(r'\D',s)
print('Letters:%d'%len(e))
