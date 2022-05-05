n=int(input())
temp=n
res=0
while n:
    d=n%10
    res=res*10+d
    n=n//10
if(temp==res):
    print('True')
else:
    print('False')