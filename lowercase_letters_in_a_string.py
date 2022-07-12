s=input()
s=list(s)
a=[]
c=0
for i in s:
    a.append(ord(i))
for i in a:
    if i>=97 and i<=122:
        c+=1
print(c)