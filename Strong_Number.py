n=int(input())
temp=n
sum=0
while n:
    fc=1
    d=n%10
    for i in range(1,d+1):
        fc=fc*i
    sum+=fc
    n=n//10
    
if temp==sum:
    print('The number',temp,'is a strong number')
else:
    print('The number',temp,'is not a strong number')