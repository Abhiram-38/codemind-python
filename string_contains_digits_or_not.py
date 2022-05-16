n=int(input())
while(n>=0):
    v=input()
    c=0
    for i in v:
        if(i.isdigit()):
            c+=1
    if(c>0):
        print('Yes')
    else:
        print('No')
    n-=1
