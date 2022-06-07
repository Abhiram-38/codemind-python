s=str(input())
a=[]
for i in s:
    a.append(i)
b=set(a)
if len(a)==len(b):
    print('True')
else:
    print('False')