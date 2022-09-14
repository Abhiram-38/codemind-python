def fun(n):
    r=0
    temp=n
    while n:
        d=n%10
        r=r*10+d
        n=n//10
    if r==temp:
        return 1
    else:
        return 0
n=int(input())
n1=n+1
n2=n-1
while n1:
    if fun(n1):
        break
    n1+=1
while n2:
    if fun(n2):
        break
    n2-=1
if abs(n1-n)>abs(n2-n):
    print(n2)
elif abs(n1-n)<abs(n2-n):
    print(n1)
else:
    print(n2,n1)