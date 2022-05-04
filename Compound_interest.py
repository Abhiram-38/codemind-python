import math
p,r,t=map(int,input().split())
d=math.pow(1+r/100,t)
ci=p*d
print("%0.2f"%ci)