r,c=map(int,input().split())
es,os=0,0
for i in range(r):
    a=list(map(int,input().split()))
    for i in a:
        if i%2==0:
            es+=i
        else:
            os+=i
print(es,os)