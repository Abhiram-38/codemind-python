s=str(input())
n=int(input())
s=list(s)
c=s.count('a')
if(n%len(s)==0):
    res1=n//len(s)
    print(res1*c)
else:
    x=0
    res1=n//len(s)
    res2=n%len(s)
    for i in range(res2):
        if s[i]=='a':
            x+=1
    print((res1*c)+x)

