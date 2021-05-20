c = int(input())
list1 = []
list3 = []
for i in range(c):
    list2 = list(map(int,input().split()))
    list2 = (list2[1:])
    average = sum(list2)/len(list2)
    num = 0
    for j in range(len(list2)):
        if list2[j]>average:
            num = num+1
    list3.append(num/len(list2)*100)

for i in range(c):
    print("%0.3f"%list3[i],end="")
    print("%")