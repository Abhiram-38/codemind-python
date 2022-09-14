a,b=map(int,input().split())
arr2=[]
for i in range(a):
    s=0
    arr=list(map(int,input().split()))
    x=sum(arr)
    arr2.append(x)
print(max(arr2))