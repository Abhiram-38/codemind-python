def fab(n):
    if n==0 or n==1:
        return 1
    a=0
    b=1
    while True:
        c=a+b
        if c==n:
            return 1
        a=b
        b=c
        if c>n:
            return 0
n=int(input())
if(fab(n)):
    print('True')
else:
    print('False')