n=int(input())
a=[]
while n:
    d=n%10
    a.append(d)
    n=n//10
print(max(a))