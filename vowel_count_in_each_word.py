s=input()
s=s.lower()
s=s.split(' ')
a=[]
for j in s:
    c=0
    x=list(j)
    for i in x:
        if i=='a'or i=='e' or i=='i' or i=='o' or i=='u':
            c+=1
    a.append(c)
print(*a)