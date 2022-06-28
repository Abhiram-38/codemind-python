def fun(n):
    s=0
    while n:
        d=n%10
        s+=d
        n=n//10
    return s
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=fun(i)
print(s)