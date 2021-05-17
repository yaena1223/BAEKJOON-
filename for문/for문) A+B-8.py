import sys
T = int(input())
sum = []
listA = []
listB = []
for i in range(T):
    A, B = map(int,sys.stdin.readline().split())
    sum.append(A+B)
    listA.append(A)
    listB.append(B)

for i in range(T):
    print("Case #%d: %d + %d = %d"%(i+1,listA[i],listB[i],sum[i]))