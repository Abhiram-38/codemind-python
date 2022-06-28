x=int(input())
a=list(map(int,input().split()))
av=sum(a)//len(a)
c=0
for i in a:
    if i>=av:
        c+=1
print(c)