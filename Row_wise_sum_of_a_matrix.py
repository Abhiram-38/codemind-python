a,b=map(int,input().split())
arr2=[]
for i in range(a):
    arr=list(map(int,input().split()))
    x=sum(arr)
    arr2.append(x)
print(*arr2)