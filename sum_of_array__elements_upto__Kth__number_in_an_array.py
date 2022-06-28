n=int(input())
a=list(map(int,input().split()))
x=int(input())
s=0
for i in a:
    if i<=x:
        s+=i
print(s)