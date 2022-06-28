x=int(input())
a=list(map(int,input().split()))
e,o=[],[]
for i in a:
    if i%2:
        o.append(i)
    else:
        e.append(i)
print(*o,end=' ')
print(*e)