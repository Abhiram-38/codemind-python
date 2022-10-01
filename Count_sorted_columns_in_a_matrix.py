r,c=map(int,input().split())
a=[]
d=0
for i in range(r):
    a.append(list(map(int,input().split())))
for i in range(c):
    b=[]
    for j in range(r):
        b.append(a[j][i])
    x=sorted(b)
    x=x[::-1]
    if b==sorted(b) or b==x:
        d+=1
print(d)
