n=int(input())
arr=list(map(int,input().split()))
a=b=0
for i in range(0,n-2,2):
    a+=1
    if(arr[i+1]>arr[i] and arr[i+1]>arr[i+2]):
        b+=1
if a==b:
    print(a)
else:
    print(-1)