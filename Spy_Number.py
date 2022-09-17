n=int(input())
t=n
s=0
c=1
while n!=0:
    r=n%10
    s=s+r
    c=c*r
    n//=10
if s==c:
    print("Spy Number")
else:
    print("Not Spy Number")
    
