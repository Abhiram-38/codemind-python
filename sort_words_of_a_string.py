s=input()
s=s.split(' ')
for i in s:
    x=list(i)
    a=[]
    for i in x:
        if ord(i)>=97 and ord(i)<=122:
            a.append(i)
    a.sort()
    d=0
    for k in range(0,len(x)):
        if x[k] not in a:
            print(x[k],end='')
        else:
            print(a[d],end='')
            d+=1
    print(end=' ')