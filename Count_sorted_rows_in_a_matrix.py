a,b=map(int,input().split())
c=0
for i in range(a):
    arr=list(map(int,input().split()))
    x=sorted(arr)
    if(x==arr or x==arr[::-1]):
        c+=1
print(c)