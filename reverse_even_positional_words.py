s=input()
s=s.split(" ")
for i in range(0,len(s)):
    if i%2==0:
        s[i]=s[i][::-1]
print(*s)