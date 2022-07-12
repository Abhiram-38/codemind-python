s=input()
s=s.split(' ')
x=s[0]
y=s[-1]
x=list(x)
x.sort()
y=list(y)
y.sort()
print(min(x),max(y))
