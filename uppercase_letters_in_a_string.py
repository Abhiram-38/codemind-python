n=str(input())
count=0
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        count+=1
print(count)