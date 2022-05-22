n=int(input())
a=n*n
b=0
e=0
while n:
    d=n%10
    b=b*10+d
    n=n//10
c=b*b
while c:
    d=c%10
    e=e*10+d
    c=c//10
if e==a:
    print('True')
else:
    print('False')