t=int(input())
while t:
    n=str(input())
    n=int(n,2)
    print(oct(n)[2::])
    t-=1