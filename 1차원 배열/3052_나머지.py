list = [0]*10
namuji = [0]*10
for i in range(10):
    list[i] = int(input())
    namuji[i] = list[i]%42
list2 = []
cnt = 0
for i in range(10):
    if namuji[i] not in list2:
        cnt = cnt+1
        list2.append(namuji[i])

print(cnt)