s=input()
s=s.split(' ')
x=0
y=0
for i in s:
    x+=ord(max(i))
    y+=ord(min(i))
print(abs(x-y))