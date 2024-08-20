x=int(input("enter the odd no"))
if x%2==0:
    x+=1
y=x//2
z=1
n=x
for i in range(y,0,-1):
    a=i*" "
    print(a,end="")
    print(z*"*")
    z+=2
for j in range(0,y+1):
    q=j*" "
    print(q,end="")
    print(n*"*")
    n-=2

