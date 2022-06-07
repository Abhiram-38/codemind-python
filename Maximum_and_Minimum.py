n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    if i==a.count(i):
        x.append(i)
if len(x)==0:
    print('-1')
else:
    print(min(x),max(x))