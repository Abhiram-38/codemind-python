n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,len(a)-1):
    if a[i]%2==0 and a[i+1]%2 and a[i-1]%2:
        c+=1
print(c)