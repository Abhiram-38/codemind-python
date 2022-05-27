t=int(input())
while t:
    n=int(input())
    for i in range(1,n):
        if n==i*i:
            print('True')
            break
    else:
        print('False')
    t-=1