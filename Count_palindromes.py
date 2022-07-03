def fun(n):
    res=0
    while n:
        d=n%10
        res=res*10+d
        n=n//10
    return res
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if fun(i)==i:
        c+=1
print(c)