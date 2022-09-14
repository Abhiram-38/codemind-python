n=int(input())
s=0
while n:
    d=n%10
    s+=d*d
    n=n//10
    if n==0 and s>9:
        n=s
        s=0
if s!=1:
    print(False)
else:
    print(True)