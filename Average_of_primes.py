def fun(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if fun(i):
        b.append(i)
x=sum(b)/len(b)
print("{0:0.2f}".format(x))