def rec(i,n,f):
    
    if f!=n:
        f+=1
        i+=f
        return rec(i,n,f)


    elif f==n:
        return i
print(rec(0,1,0))
   
