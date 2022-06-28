x=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i==0:
        c+=1
    if i%2==0:
        c+=1
if c==x:
    print(True)
else:
    print(False)