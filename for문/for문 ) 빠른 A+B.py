import sys
sum = []
num = int(input())
for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    sum.append(a+b)

for i in range(num):
    print(sum[i])