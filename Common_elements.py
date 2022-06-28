m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
for i in a:
    if i in b and i not in x:
        x.append(i)
print(*x)