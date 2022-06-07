def fun(n):
    c=0
    while n:
        n=n//10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    x.append(fun(i))
y=max(x)
print(x.count(y))