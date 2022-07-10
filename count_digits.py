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
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(fun(i))
print(*b)