s=input()
s=s.lower()
s=s.split(' ')
for i in s:
    x=list(i)
    print(min(x),max(x),end=' ')