t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    x=(n*(n+1))//2
    print(x-sum(a))
    t-=1