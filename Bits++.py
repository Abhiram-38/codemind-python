n=int(input())
x=0
for i in range(0,n):
    p=input()
    if '+' in p:
        x+=1
    elif '-' in p:
        x-=1
print(x)