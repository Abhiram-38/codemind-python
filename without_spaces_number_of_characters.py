n=str(input())
count=0
for i in n:
    if ord(i)!=32:
        count+=1
print(count)