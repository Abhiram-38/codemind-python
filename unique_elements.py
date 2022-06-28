n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if a.count(i)>=1 and i not in b:
        print(i,end=' ')
        b.append(i)