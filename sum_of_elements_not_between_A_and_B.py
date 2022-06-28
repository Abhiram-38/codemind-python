x=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
y=[]
for i in a:
    if i<m or i>n:
        y.append(i)
print(sum(y))