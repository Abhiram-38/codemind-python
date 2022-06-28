n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    if i not in x:
        print(i,a.count(i),end=' ')
        x.append(i)