n=int(input())
max=0
while(n):
    d=n%10
    if(max<d):
        max=d
    n=n//10
print(max)