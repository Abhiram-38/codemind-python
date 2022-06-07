a=input()
b=input()
a=a.lower()
b=b.lower()
if len(a)==len(b):
    a=sorted(a)
    b=sorted(a)
    if a==b:
        print('True')
    else:
        print('False')
else:
    print('False')