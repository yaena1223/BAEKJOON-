sum = []
a = -1
b = -1
while(a!=0 and b!=0):
    a,b = map(int,input().split())
    sum.append(a+b)

for i in range(len(sum)-1):
    print(sum[i])


