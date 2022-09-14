s=input()
s=s.lower()
s=s.split(' ')
s1=s[0]
b=0
for i in s1:
    a=0
    for j in s:
        if i in j:
            a+=1
        else:
            a=0
    if a==len(s):
        b+=1
print(b)