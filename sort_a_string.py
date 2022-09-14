s=input()
a=[]
for i in s:
    if i.isalpha():
        a.append(i)
a.sort()
k=0
for i in s:
    if i.isalpha():
        i=a[k]
        k+=1
    print(i,end='')