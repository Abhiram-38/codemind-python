t=int(input())
for i in range(t):
    n=int(input())
    s=str(input())
    s=list(s)
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    else:
        print(-1)