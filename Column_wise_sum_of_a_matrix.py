r,c=map(int,input().split())
a=[]
b=[]
for i in range(r):
    a.append(list(map(int,input().split())))
for i in range(c):
    sum1=0
    sum2=0
    for j in range(r):
        ##sum1+=a[i][j]
        sum2+=a[j][i]
    ##b.append(sum1)
    b.append(sum2)
print(*b)