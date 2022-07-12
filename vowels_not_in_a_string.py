s=input()
s=list(s)
a=['a','e','i','o','u']
b=[]
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        b.append(i)
b=set(b)
if len(b)==5:
    print('0')
else:
    for i in a:
        if i not in b:
            print(i,end=' ')