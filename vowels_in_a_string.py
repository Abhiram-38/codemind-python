s=input()
c=input()
s=list(s)
for i in range(len(s)):
    if s[i]==c:
        print(True)
        print(i)
        break
else:
    print(False)
    
