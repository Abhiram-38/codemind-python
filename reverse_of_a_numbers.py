n=int(input())
res=0
while(n):
    d=n%10
    res=res*10+d
    n=n//10
print(res)    