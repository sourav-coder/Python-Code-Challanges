t=(1,2,3,4,5,6,7,8,9,10)
func=lambda :print(tuple(i for i in t if i%2==0))

func()
