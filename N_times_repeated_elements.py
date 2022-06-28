n=int(input())
a=list(map(int,input().split()))
x=int(input())
y=[]
for i in a:
    if a.count(i)==x:
        y.append(i)
if len(y)==0:
    print(-1)
else:
    y=set(y)
    y=list(y)
    print(*y)