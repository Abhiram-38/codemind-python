s=input()
s=s.lower()
a=[]
for i in s:
    a.append(i)
for i in s:
    if a.count(i)==1:
        print(i)
        break
else:
    print(-1)