def fun1(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
def fun2(n):
    temp=n
    res=0
    while n:
        d=n%10
        res=res*10+d
        n=n//10
    if res==temp:
        return 1
    else:
        return 0
n=int(input())
n=n+1
while True:
    if fun1(n) and fun2(n):
        print(n)
        break
    n+=1