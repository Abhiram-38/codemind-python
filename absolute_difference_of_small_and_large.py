s=input()
s=s.split(' ')
for i in s:
    x=max(i)
    y=min(i)
    print(abs(ord(x)-ord(y)),end=' ')