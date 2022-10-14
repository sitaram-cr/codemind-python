a,b,c=map(int,input().split())
s=(a+b+c)/2
s1=s*(s-a)*(s-b)*(s-c)
s2=s1**0.5
r='{:.2f}'.format(s2)
print(r)