a=list(map(str,input().split(',')))


for s in a:
    
    upper=0
    lower=0
    sp=0
    digit=0
    if len(s)>=6 and len(s)<=12:

        for i in s:
            if i.isdigit():
                digit+=1
            if i.islower():
                lower+=1
            if i.isupper():
                upper+=1
            if i=='$' or i=='#' or i=='@':
                sp+=1
            if upper>=1 and lower>=1 and digit>=1 and sp>=1:
                f=1
                print(s,end=',')
                break

            



            





            




