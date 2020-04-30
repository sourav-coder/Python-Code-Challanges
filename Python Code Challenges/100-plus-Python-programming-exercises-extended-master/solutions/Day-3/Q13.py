s=input()
import string
d=0
c=0
for i in s:
    if i!=' ' or i!=string.punctuation:
        if i.isdigit():d+=1
        elif i.isalpha():c+=1

print('LETTERS: ',c)
print('DIGITS: ',d)