n=int(input())
temp=n
res=c=0
while n:
    n=n//10
    c+=1
n=temp
while n:
    d=n%10
    res+=d**c
    n=n//10
    c-=1
if res==temp:
    print(True)
else:
    print(False)