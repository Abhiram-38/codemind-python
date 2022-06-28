x=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
y=[]
for i in a:
    if i>=m and i<=n:
        y.append(i)
if len(y)==0:
    print(-1)
else:
    print(max(y))