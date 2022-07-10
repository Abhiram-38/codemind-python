def fun(n):
    c=0
    if n<0:
        n=-n
    if n==0:
        return 1
    while n:
        c+=1
        n=n//10
    return c
n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if fun(i)==m:
        c+=1
print(c)