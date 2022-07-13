s=input()
s=s.lower()
s=list(s)
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
a.sort()
st='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'
for i in a:
    if i==' ':
        continue
    st+=i
print(st)