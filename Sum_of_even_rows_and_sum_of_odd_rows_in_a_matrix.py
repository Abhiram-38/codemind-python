r,c=map(int,input().split())
es,os=0,0
for i in range(r):
    a=list(map(int,input().split()))
    if i%2==0:
        es+=sum(a)
    else:
        os+=sum(a)
print(es,os)