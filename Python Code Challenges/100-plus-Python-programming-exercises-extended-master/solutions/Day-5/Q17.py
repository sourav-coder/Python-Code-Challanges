number_of_transactions=int(input())
amt=0
while number_of_transactions>0:
    number_of_transactions-=1

    a,b=map(str,input().split())
    b=int(b)
    if a=='W' and b<=amt:amt-=b
    elif a=='D':amt+=b
    else:print('Not enough balance Please try again')

print(amt)
    
    