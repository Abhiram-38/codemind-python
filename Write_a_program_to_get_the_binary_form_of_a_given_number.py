t=int(input())
while t:
    n=str(input())
    n=int(n)
    print(bin(n)[2::])
    t-=1