n=int(input())
temp=n
sum=0
while(n):
    d=n%10
    sum+=d
    n=n//10
if(temp%sum==0):
    print('True')
else:
    print('False')