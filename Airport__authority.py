n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
m=int(input())
c=0
for i in a:
    if i<=m:
        c+=1
    else:
        c+=2
print(c)