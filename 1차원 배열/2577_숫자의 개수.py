a = int(input())
b = int(input())
c = int(input())
ans = a*b*c
ans = str(ans)
list = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(ans)):
    for j in range(10):
        if ans[i] == str(j):
            list[j] = list[j]+1

for i in range(10):
    print(list[i])

