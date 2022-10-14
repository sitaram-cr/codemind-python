num=int(input())
for i in range(1,num):
    r=i*(i+1)
    if (r==num):
        print("YES")
        break
else:
    print("NO")