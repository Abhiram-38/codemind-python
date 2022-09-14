n=int(input())#12
x=n*n#144
y=0
while n:
    d=n%10
    y=y*10+d
    n=n//10
z=y*y
res=0
while z:
    d=z%10
    res=res*10+d
    z=z//10
if x==res:
    print(True)
else:
    print(False)