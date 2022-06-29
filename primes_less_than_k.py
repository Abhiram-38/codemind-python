def fun(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
x=int(input())
c=0
for i in a:
    if fun(i) and i<=x:
        c+=1
print(c)