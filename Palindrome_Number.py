t=int(input())
while t:
    n=int(input())
    n=str(n)
    if n==n[::-1]:
        print('True')
    else:
        print('False')
    t-=1