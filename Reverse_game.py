def fun(n):
    res=0
    while n:
        d=n%10
        res=res*10+d
        n=n//10
    return res
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(fun(i))
print(*b)
