x=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i==1 or i==0:
        c+=1
if c==x:
    print(True)
else:
    print(False)