s=input()
s=list(s)
a=[]
c=0
for i in s:
    a.append(ord(i))
for i in a:
    if i>=65 and i<=90:
        c+=1
print(c)