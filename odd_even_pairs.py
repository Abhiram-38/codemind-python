n=int(input())
a=list(map(int,input().split()))
o=[]
e=[]
res=[]
for i in a:
    if i%2:
        o.append(i)
    else:
        e.append(i)
for i in range(min(len(o),len(e))):
    res.append(o[i])
    res.append(e[i])
if len(e)>len(o):
    for i in range(len(o),len(e)):
        res.append(e[i])
else:
    for i in range(len(e),len(o)):
        res.append(o[i])
if n%2:
    res.append(0)
print(*res)
    