x=int(input())
a=list(map(int,input().split()))
res=0
x=x-1
for i in a:
    if i==1:
        res+=(2**x)
    x-=1
print(res)