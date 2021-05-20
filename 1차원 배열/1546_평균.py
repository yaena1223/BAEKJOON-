n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
sum = 0
for i in range(n):
    new_score = score[i]/max_score*100
    score[i] = new_score
    sum = sum + new_score

print(sum/n)