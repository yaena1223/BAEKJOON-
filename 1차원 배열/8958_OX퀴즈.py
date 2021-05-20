n = int(input())
sum_list = []

for i in range(n):
    string = input()

    if string[0] == "O":
        sum = 1
        score = 1
    else:
        sum = 0
    for j in range(1,len(string)):
        if(string[j]=="O"):
            if(string[j-1]=="O"):
                score = score+1
            else:
                score = 1

        else :
            score = 0
        sum = sum + score

    sum_list.append(sum)

for i in range(n):
    print(sum_list[i])
