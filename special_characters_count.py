s=input()
s=list(s)
a=[]
c=0
for i in s:
    a.append(ord(i))
for i in a:
    if (i>=65 and i<=90) or (i>=97 and i<=122):
        continue
    elif i==32:
        continue
    else:
        c+=1
print(c)