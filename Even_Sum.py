n=int(input())
a=list(map(int,input().split()))
e=0
for i in a:
   if i%2==0:
       e+=i
print(e)