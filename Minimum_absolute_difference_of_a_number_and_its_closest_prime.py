def fun(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
if fun(n):
    print(0)
else:
    n1=n+1
    n2=n-1
    while True:
        if fun(n1):
            x=n1
            break
        n1+=1
    while True:
        if fun(n2):
            y=n2
            break
        n2-=1
    if abs(n1-n)>abs(n2-n):
        print(abs(n2-n))
    elif abs(n1-n)<abs(n2-n):
        print(abs(n1-n))
    else:
        print(abs(n1-n))