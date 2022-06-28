n=int(input())
a=list(map(int,input().split()))
b=[]
a
for i in a:
    if i==a.count(i) and i not in b:
        b.append(i)
if len(b)==0:
    print(-1)
else:
    x=(sum(b)/len(b))
    print("{0:0.2f}".format(x))