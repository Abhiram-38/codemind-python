n=int(input())
x=n*n
y=x
sum=0
while x:
    d=x%10
    sum+=d
    x=x//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')