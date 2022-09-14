def fun1(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
if fun1(n):
    print("prime")
else:
    print("not a prime")