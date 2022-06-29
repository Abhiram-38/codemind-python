n=int(input())
a=list(map(int,input().split()))
x=sum(a)//len(a)
if x in a:
    print(True)
else:
    print(False)