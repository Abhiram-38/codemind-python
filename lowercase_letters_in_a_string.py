n=str(input())
count=0
for i in n:
    if ord(i)>=97 and ord(i)<=122:
        count+=1
print(count)