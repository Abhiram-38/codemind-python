s=input()
s=s.lower()
a=[]
for i in s:
    if i==' ':
        continue
    if i not in a:
        a.append(i)
print(len(a))