n=int(input())
a=list(map(int,input().split()))
x=[]
y=[]
res=[]
if n%2:
    x=a[0:n//2]
    y=a[n//2+1:n]
    y=y[::-1]
    for i in range(len(x)):
        res.append(x[i])
        res.append(y[i])
    res.append(a[n//2])
    res.append(0)
else:
    x=a[0:n//2]
    y=a[n//2:n]
    y=y[::-1]
    for i in range(len(x)):
        res.append(x[i])
        res.append(y[i])
print(*res)