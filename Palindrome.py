def fun(n):
    r=0
    temp=n
    while n:
        d=n%10
        r=r*10+d
        n=n//10
    if r==temp:
        return 1
    else:
        return 0
n=int(input())
if fun(n):
    print(True)
else:
    print(False)