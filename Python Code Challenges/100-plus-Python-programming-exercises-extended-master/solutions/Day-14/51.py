def divide():
    a=5
    b=0
    try:
        print(a/b)
    except ZeroDivisionError:
        print('INF')

divide()