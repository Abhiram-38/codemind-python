n=int(input())
a=list(map(int,input().split()))
k=int(input())
x=[]
for i in a:
    if a.count(i)==k and i not in x:
        x.append(i)
if len(x)==0:
    print('-1')
else:
    print(*x)