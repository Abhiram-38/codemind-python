def fun(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n1=int(input())
n2=int(input())
a=n1+n2
x=a+1
while True:
    if(fun(x)):
        print(x-a)
        break
    x+=1
    
    