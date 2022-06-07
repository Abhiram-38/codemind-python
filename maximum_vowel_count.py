n=input()
n=n.split()
m=0
for i in n:
    c=0
    for j in i:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U':
            c+=1
    if c>m:
        m=c
print(m)