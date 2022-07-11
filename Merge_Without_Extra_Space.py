t=int(input())
while t:
    m,n=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=a+b
    c.sort()
    print(*c)
    t-=1